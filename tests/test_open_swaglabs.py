from playwright.sync_api import expect
import time


def test_login_saucedemo(page):
    #login steps are already done in the fixture
    #verify login success (products display page should be visible)	
    expect(page.locator("//span[@class='title']")).to_have_text("Products")
    print("login successful and products page is visible")

    #logout button should not be visible before clicking on three horizontal lines
    expect(page.locator('//a[@id="logout_sidebar_link"]')).not_to_be_visible()
    print("logout button is not visible before clicking on three horizontal line")

    #if we click on 3 horizontal lines on top left corner, side menu should open
    page.locator("//button[@id='react-burger-menu-btn']").click()
    print("clicked on three horizontal lines")
    
    #click on three horizontal lines
    #page.locator("//button[@id='react-burger-menu-btn']").click()
    #print("click on three horizontal lines")
    
    #check all items, about, logout and reset links are visible in side menu
    expect(page.locator("//a[@id='inventory_sidebar_link']")).to_be_visible()
    print("All items link is visible")
    expect(page.locator("//a[@id='about_sidebar_link']")).to_be_visible()
    print("About link is visible")
    expect(page.locator("//a[@id='logout_sidebar_link']")).to_be_visible()
    print("logout link is visible")
    expect(page.locator("//a[@id='reset_sidebar_link']")).to_be_visible()
    print("Reset link is visible")
    
    #check if the all items, about, logout and reset links are clickable
    expect(page.locator("//a[@data-test='inventory-sidebar-link']")).to_be_enabled()
    expect(page.locator("//a[@data-test='about-sidebar-link']")).to_be_enabled()
    expect(page.locator("//a[@data-test='logout-sidebar-link']")).to_be_enabled()
    expect(page.locator("//a[@data-test='reset-sidebar-link']")).to_be_enabled()
    print("all items, about, logout and reset links are clickable")
    
    #check if the filter option is visible
    expect(page.locator("//select[@data-test='product-sort-container']")).to_be_visible()
    print("filter option is visible")
    
    #check if the filter option is clickable
    assert page.locator("//select[@data-test='product-sort-container']").is_enabled()
    
    #check if the filter dropdown is working
    page.locator("//select[@data-test='product-sort-container']").select_option("az")
    print("filter dropdown name A to Z is working")
    time.sleep(2)
    page.locator("//select[@data-test='product-sort-container']").select_option("za")
    print("filter dropdown name Z to A is working")
    time.sleep(2)
    page.locator("//select[@data-test='product-sort-container']").select_option("lohi")
    print("filter dropdown price low to high is working")
    time.sleep(2)
    page.locator("//select[@data-test='product-sort-container']").select_option("hilo")
    print("filter dropdown price high to low is working")
    time.sleep(2)
    
    #check if inventory item is visible
    #expect(page.locator("//div[contains(@class, 'inventory_item_name')]")).to_be_visible()
    #print("one inventory item is visible")
    
    #check if all inventory items are visible
    all_items = page.locator("//div[contains(@class, 'inventory_item_name')]")
    count = all_items.count()

    for i in range(count):
        expect(all_items.nth(i)).to_be_visible()
        print(f"items {i+1} is visible")
        
    #check if the inventory items are clickable
    for i in range(count):
        expect(all_items.nth(i)).to_be_enabled()
        print(f'items {i+1} is clickable')
        
    #check if the produt image is visible
    all_images = page.locator("//img[@class='inventory_item_img']")
    count1 = all_items.count()
    
    for i in range(count1):
        expect(all_images.nth(i)).to_be_visible()
        print(f'product image {i+1} is visible')
        
    #check if the product image is clickable
    for i in range(count1):
        expect(all_images.nth(i)).to_be_enabled()
        print(f"image {i+1} is clickable")    
        
    #check if the add to cart button is visible below each item
    all_add_to_cart = page.locator("//button[contains(@data-test, 'add-to-cart')]")
    count2 = all_add_to_cart.count()
    print(f"total items found: {count2}")
    
    for i in range(count2):
        expect(all_add_to_cart.nth(i)).to_be_visible()
        print(f"add to cart button {i+1} is visible")
        
    #check if add to cart button is clickable
    for i in range(count2):
        expect(all_add_to_cart.nth(i)).to_be_enabled()
        print(f"add to cart button {i+1} is clickable")
        
    #check if the inventory item price is visible below each item
    all_price = page.locator("//div[@data-test='inventory-item-price']")
    count3 = all_price.count()
    
    for i in range(count3):
        expect(all_price.nth(i)).to_be_visible()
        print(f"price of item {i+1} is visible")
        
    #check if we click on add to cart option the item should get added to the cart
    #first we are getting static list of 6 items
    for i in range(count2):
        btn = page.locator("//button[contains(@data-test, 'add-to-cart')]").first
        btn.click()
        print(f"item {i+1} is added to the cart")
        time.sleep(1)

    #check if remove button is visible on the product after adding item to the cart
        expect(page.locator("//button[text()='Remove']").first).to_be_visible()
        print(f"remove button is visible on the product {i+1} after adding to the cart")
    
    #check if inventory item description is visible on the products page
    descriptions = page.locator("//div[@data-test='inventory-item-desc']")
    count4 = descriptions.count()

    for i in range(count4):
        expect(page.locator("//div[@data-test='inventory-item-desc']").nth(i)).to_be_visible()
        print(f"inventory item description of {i+1} is visible")
        
    #check if the cart option is visible and clickable
    expect(page.locator("//div[@id='shopping_cart_container']")).to_be_visible()
    print("cart option is visible")
    expect(page.locator("//div[@id='shopping_cart_container']")).to_be_enabled()
    print("cart option is clickable")
    
    #check after clicking on a cart button, the cart page should open and it should show all the items
    page.locator("//span[@class='shopping_cart_badge']").click()
    print("clicked on cart option")
    expect(page.locator("//span[@class='shopping_cart_badge']")).to_have_text("6")
    print("cart page is opened and it is showing all the items added to the cart")
    
    #check if continue shopping button is visible on the cart page
    expect(page.locator("//button[@data-test='continue-shopping']")).to_be_visible()
    print("continue shopping button is visible on the cart page")

    #check if Your Cart, QTY and description headings are visible on the cart page
    expect(page.locator("//span[@data-test='title']")).to_be_visible()
    print("Your Cart heading is visible on the cart page")
    expect(page.locator("//div[@data-test='cart-quantity-label']")).to_be_visible()
    print("QTY heading is visible on the cart page")
    expect(page.locator("//div[@data-test='cart-desc-label']")).to_be_visible()
    print("description heading is visible on the cart page")
    

    #check if checkout button is visible and clickable on the cart page
    expect(page.locator("//button[@data-test='checkout']")).to_be_visible()
    print("checkout button is visible")
    expect(page.locator("//button[@data-test='checkout']")).to_be_enabled()
    print("checkout button is clickable")
    
    #check if remove button is visible and clickable on the cart page
    remove_button_cart = page.locator("//button[contains(@data-test,'remove-')]")
    count5 = remove_button_cart.count()
    for i in range(count5):
        expect(remove_button_cart.nth(i)).to_be_visible()
        print(f"remove button for {i+1} items added to the cart is visible")
        expect(remove_button_cart.nth(i)).to_be_enabled()
        print(f"remove button for {i+1} items added to the cart is clickable")
    
    #check after clicking on the checkout button the checkout page should open and it should show the heading "Checkout: Your Information"
    page.locator("//button[@data-test='checkout']").click()
    print("clicked on checkout button")
    expect(page.locator("//span[@data-test='title']")).to_have_text("Checkout: Your Information")
    print("after clicking on the checkout button the checkout page is showing the heading \"Checkout: Your Information\"")
            
    
    #check if the first name, last name and postal code fields are visible and clickable on the checkout page
    expect(page.locator("//input[@data-test='firstName']")).to_be_visible()
    print("first name field is visible")
    expect(page.locator("//input[@data-test='firstName']")).to_be_enabled()
    print("first name field is clickable")
    expect(page.locator("//input[@data-test='lastName']")).to_be_visible()
    print("last name field is visible")
    expect(page.locator("//input[@data-test='lastName']")).to_be_enabled()
    print("last name field is clickable")
    expect(page.locator("//input[@data-test='postalCode']")).to_be_visible()
    print("postal code field is visible")
    expect(page.locator("//input[@data-test='postalCode']")).to_be_enabled()
    print("postal code field is clickable")
    
    #check if the cancel and continue buttons are visible and clickable on the checkout pages
    expect(page.locator("//button[@data-test='cancel']")).to_be_visible()
    print("cancel button is visible")
    expect(page.locator("//button[@data-test='cancel']")).to_be_enabled()
    print("cancel button is clickable")
    expect(page.locator("//input[@data-test='continue']")).to_be_visible()
    print("continue button is visible")
    expect(page.locator("//input[@data-test='continue']")).to_be_enabled()
    print("continue button is clickable")
    
    #check if we fill the first name, last name and postal code fields and click on continue button, the next page should open
    page.locator("//input[@data-test='firstName']").fill("omkar")
    page.locator("//input[@data-test='lastName']").fill("bhabad")
    page.locator("//input[@data-test='postalCode']").fill("411033")
    print("first name, last name and postal code are entered")
    
    page.locator("//input[@data-test='continue']").click()
    print("clicked on continue button")
    
    expect(page.locator("//span[@data-test='title']")).to_have_text("Checkout: Overview")
    expect(page.locator("//div[@class='summary_info']")).to_be_visible()
    print("after clicking on continue button the next page is opened and it is showing the heading 'Checkout: Overview' and summary information is visible")
    
    #if we click on continue button without entering the first name, last name and postal code fields, it should show error message
    page.locator("//div[@id='shopping_cart_container']").click()
    page.locator("//button[@data-test='checkout']").click()
    page.locator("//input[@data-test='firstName']").fill("")
    page.locator("//input[@data-test='lastName']").fill("")
    page.locator("//input[@data-test='postalCode']").fill("")
    print("first name, last name and postal code fields are empty")
    
    page.locator("//input[@data-test='continue']").click()
    print("clicked on continue button without entering first name, last name and postal code")
    
    expect(page.locator("//h3[@data-test='error']")).to_have_text("Error: First Name is required")
    print("error message is visible: 'Error: First Name is required'")
    
    #close browser
    time.sleep(3)

    