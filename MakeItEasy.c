#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_USERS 100
#define MAX_PRODUCTS 110
#define MAX_NOTIFICATIONS 5
#define MAX_TRADE_PRODUCTS 100
#define MAX_TRADES 100
#define MAX_CHAT_LENGTH 256
#define MAX_CHAT_MESSAGES 10

typedef struct {
    char username[50];
    char password[50];
    char language[10];
    double balance;
    char purchased_items[10][50];
    int purchased_count;
} User;

typedef struct {
    char product_name[50];
    double price;
    int stock;
    char seller_name[50];
    int daily_sales;
    double rating;
    int rating_count;
} Product;

typedef struct {
    char trade_item[50];
    char trade_for[50];
    char owner[50];
} Trade;

typedef struct {
    char sender[50];
    char receiver[50];
    char messages[MAX_CHAT_MESSAGES][MAX_CHAT_LENGTH];
    int message_count;
} Chat;

User users[MAX_USERS];
Product products[MAX_PRODUCTS];
Trade trades[MAX_TRADE_PRODUCTS];
Chat chats[MAX_USERS];
int user_count = 0, product_count = 0, trade_count = 0, chat_count = 0;

User current_user = {"guest", "password", "en", 100.0, {""}, 0};

// Yardımcı fonksiyon bildirimleri
void list_products(void);
int prompt_continue(void);

void initialize_users() {
    strcpy(users[0].username, "Alice");
    strcpy(users[0].password, "pass123");
    users[0].balance = 1000.0;
    users[0].purchased_count = 0;
    
    strcpy(users[1].username, "Bob");
    strcpy(users[1].password, "pass123");
    users[1].balance = 1000.0;
    users[1].purchased_count = 0;
    
    strcpy(users[2].username, "Charlie");
    strcpy(users[2].password, "pass123");
    users[2].balance = 1000.0;
    users[2].purchased_count = 0;
    
    user_count = 3;
}

void initialize_products() {
    // Ürün örnekleri aynı kalacak, sadece ürün sayısını kontrol edelim
    // ... (mevcut ürün initializations kodu)
    product_count = 11;
}

// Eksik olan yardımcı fonksiyon
int prompt_continue() {
    printf("\nPress 1 to continue: ");
    int choice;
    scanf("%d", &choice);
    return choice;
}

void list_products() {
    printf("\n=== Market Products ===\n");
    for (int i = 0; i < product_count; i++) {
        printf("%d. %s - $%.2f - Stock: %d - Seller: %s\n  Daily Sales: %d - Rating: %.1f (%d ratings)\n",
               i + 1, products[i].product_name, products[i].price, products[i].stock, 
               products[i].seller_name, products[i].daily_sales, products[i].rating, 
               products[i].rating_count);
    }
}

void buy_product() {
    list_products();
    printf("\nEnter the product number to purchase (0 to cancel): ");
    int choice;
    scanf("%d", &choice);
    
    if (choice == 0) {
        printf("Purchase cancelled.\n");
        return;
    }
    
    choice--;
    if (choice < 0 || choice >= product_count) {
        printf("Invalid choice!\n");
        return;
    }

    printf("Enter the quantity: ");
    int quantity;
    scanf("%d", &quantity);

    if (quantity <= 0) {
        printf("Invalid quantity!\n");
        return;
    }

    if (quantity > products[choice].stock) {
        printf("Not enough stock available!\n");
        return;
    }

    double total_price = products[choice].price * quantity;
    if (total_price > current_user.balance) {
        printf("Insufficient balance!\n");
        return;
    }

    if (current_user.purchased_count >= 10) {
        printf("Purchase history is full!\n");
        return;
    }

    current_user.balance -= total_price;
    products[choice].stock -= quantity;
    products[choice].daily_sales += quantity;
    strcpy(current_user.purchased_items[current_user.purchased_count], products[choice].product_name);
    current_user.purchased_count++;

    printf("Purchase successful! You bought %d x %s for $%.2f.\n", 
           quantity, products[choice].product_name, total_price);
}

void sell_product() {
    if (product_count >= MAX_PRODUCTS) {
        printf("Market is full, cannot add more products!\n");
        return;
    }

    char product_name[50];
    double price;
    int stock;

    printf("Enter the name of the product you want to sell: ");
    getchar();
    fgets(product_name, sizeof(product_name), stdin);
    product_name[strcspn(product_name, "\n")] = 0;

    printf("Enter the price of the product: ");
    if (scanf("%lf", &price) != 1 || price <= 0) {
        printf("Invalid price!\n");
        return;
    }

    printf("Enter the stock quantity: ");
    if (scanf("%d", &stock) != 1 || stock <= 0) {
        printf("Invalid stock quantity!\n");
        return;
    }

    strcpy(products[product_count].product_name, product_name);
    products[product_count].price = price;
    products[product_count].stock = stock;
    strcpy(products[product_count].seller_name, current_user.username);
    products[product_count].daily_sales = 0;
    products[product_count].rating = 0.0;
    products[product_count].rating_count = 0;

    product_count++;
    printf("Product successfully added to the market!\n");
}

void add_trade_item() {
    if (trade_count >= MAX_TRADE_PRODUCTS) {
        printf("Trade market limit reached!\n");
        return;
    }

    char item[50], trade_for[50];
    
    printf("Enter the item you want to trade: ");
    getchar();
    fgets(item, sizeof(item), stdin);
    item[strcspn(item, "\n")] = 0;

    printf("Enter the item you want in exchange: ");
    fgets(trade_for, sizeof(trade_for), stdin);
    trade_for[strcspn(trade_for, "\n")] = 0;

    strcpy(trades[trade_count].trade_item, item);
    strcpy(trades[trade_count].trade_for, trade_for);
    strcpy(trades[trade_count].owner, current_user.username);
    trade_count++;

    printf("Trade offer added successfully!\n");
}

void list_trades() {
    if (trade_count == 0) {
        printf("\n=== Trade Market ===\nNo trades available.\n");
        return;
    }

    printf("\n=== Trade Market ===\n");
    for (int i = 0; i < trade_count; i++) {
        printf("%d. %s (Owner: %s) for %s\n", 
               i + 1, trades[i].trade_item, trades[i].owner, trades[i].trade_for);
    }
}

void profile() {
    printf("\n=== Profile ===\n");
    printf("Username: %s\n", current_user.username);
    printf("Balance: $%.2f\n", current_user.balance);
    
    if (current_user.purchased_count > 0) {
        printf("Purchased Items:\n");
        for (int i = 0; i < current_user.purchased_count; i++) {
            printf("- %s\n", current_user.purchased_items[i]);
        }
    } else {
        printf("No purchased items.\n");
    }

    printf("\n1. Add Balance\n2. Back\nEnter your choice: ");
    int choice;
    scanf("%d", &choice);

    if (choice == 1) {
        double amount;
        printf("Enter amount to add: ");
        if (scanf("%lf", &amount) == 1 && amount > 0) {
            current_user.balance += amount;
            printf("Balance updated! New Balance: $%.2f\n", current_user.balance);
        } else {
            printf("Invalid amount!\n");
        }
    }
}

void chat_system() {
    printf("\n=== Chat System ===\n");
    if (user_count <= 1) {
        printf("No other users available to chat with.\n");
        return;
    }

    printf("Users you can chat with:\n");
    for (int i = 0; i < user_count; i++) {
        if (strcmp(users[i].username, current_user.username) != 0) {
            printf("- %s\n", users[i].username);
        }
    }

    printf("Enter the username of the person you want to chat with: ");
    char username[50];
    getchar();
    fgets(username, sizeof(username), stdin);
    username[strcspn(username, "\n")] = 0;

    // Kullanıcı kontrolü
    int valid_user = 0;
    for (int i = 0; i < user_count; i++) {
        if (strcmp(users[i].username, username) == 0) {
            valid_user = 1;
            break;
        }
    }

    if (!valid_user) {
        printf("User not found!\n");
        return;
    }

    int chat_index = -1;
    for (int i = 0; i < chat_count; i++) {
        if (strcmp(chats[i].receiver, username) == 0) {
            chat_index = i;
            break;
        }
    }

    if (chat_index == -1) {
        if (chat_count >= MAX_USERS) {
            printf("Chat system is full!\n");
            return;
        }
        strcpy(chats[chat_count].sender, current_user.username);
        strcpy(chats[chat_count].receiver, username);
        chats[chat_count].message_count = 0;
        chat_index = chat_count;
        chat_count++;
    }

    printf("\nChat history:\n");
    for (int i = 0; i < chats[chat_index].message_count; i++) {
        printf("%s: %s\n", chats[chat_index].sender, chats[chat_index].messages[i]);
    }

    while (1) {
        printf("\nEnter your message (or 'exit' to leave): ");
        char message[MAX_CHAT_LENGTH];
        fgets(message, sizeof(message), stdin);
        message[strcspn(message, "\n")] = 0;

        if (strcmp(message, "exit") == 0) {
            break;
        }

        if (chats[chat_index].message_count < MAX_CHAT_MESSAGES) {
            strcpy(chats[chat_index].messages[chats[chat_index].message_count], message);
            chats[chat_index].message_count++;
            printf("Message sent!\n");
        } else {
            printf("Chat message limit reached!\n");
        }
    }
}

void technical_support() {
    printf("\n=== Technical Support ===\n");
    printf("1. Submit a Complaint\n2. Submit Feedback\n3. Contact Support\n"
           "4. Report an Issue\n5. Back\nEnter your choice: ");
    
    int choice;
    if (scanf("%d", &choice) != 1) {
        printf("Invalid input!\n");
        return;
    }

    getchar();
    char input[MAX_CHAT_LENGTH];
    
    switch(choice) {
        case 1:
            printf("Enter your complaint: ");
            fgets(input, sizeof(input), stdin);
            printf("Complaint submitted successfully!\n");
            break;
        case 2:
            printf("Enter your feedback: ");
            fgets(input, sizeof(input), stdin);
            printf("Feedback submitted successfully!\n");
            break;
        case 3:
            printf("Enter the issue you want to contact support about: ");
            fgets(input, sizeof(input), stdin);
            printf("Your message has been sent to support. We will get back to you shortly.\n");
            break;
        case 4:
            printf("Enter the issue to report: ");
            fgets(input, sizeof(input), stdin);
            printf("Issue reported successfully. Thank you for your feedback!\n");
            break;
        case 5:
            return;
        default:
            printf("Invalid choice!\n");
    }
}

void main_menu() {
    while (1) {
        printf("\n=== Main Menu ===\n");
        printf("1. Market\n2. Sell Product\n3. Add Trade Item\n4. View Trade Market\n"
               "5. Profile\n6. Chat System\n7. Technical Support\n8. Exit\n");
        printf("Enter your choice: ");
        
        int choice;
        if (scanf("%d", &choice) != 1) {
            printf("Invalid input!\n");
            while (getchar() != '\n'); // Buffer temizleme
            continue;
        }

        switch (choice) {
            case 1:
                buy_product();
                break;
            case 2:
                sell_product();
                break;
            case 3:
                add_trade_item();
                break;
            case 4:
                list_trades();
                break;
            case 5:
                profile();
                break;
            case 6:
                chat_system();
                break;
            case 7:
                technical_support();
                break;
            case 8:
                printf("Goodbye!\n");
                return;
            default:
                printf("Invalid choice. Please select a valid option.\n");
        }
    }
}

int main() {
    initialize_users();
    initialize_products();
    main_menu();
    return 0;
}
