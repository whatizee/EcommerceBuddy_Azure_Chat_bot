import random
import openpyxl

# List of common product names
product_names = [
    "Smartphone", "Laptop", "Headphones", "Coffee Maker", "Backpack",
    "Running Shoes", "Sunglasses", "Watch", "Fitness Tracker",
    "Bluetooth Speaker", "Gaming Console", "Vacuum Cleaner",
    "Smartwatch", "Dishwasher", "Refrigerator", "Electric Toothbrush", "Hair Dryer",
    "Coffee Grinder", "Toothpaste", "Hiking Boots", "Back Massager", "Handheld Vacuum",
    "Yoga Mat", "Food Processor", "Car Vacuum", "Wireless Mouse", "Electric Shaver",
    "Soundbar", "Digital Scale", "Air Purifier", "Projector", "Guitar",
    "Desk Chair", "Camping Tent", "Instant Pot", "Kindle", "Wireless Earbuds",
    "Soda Maker", "Air Conditioner", "Robot Vacuum", "Juicer", "Indoor Plants",
    "Cordless Drill", "Water Bottle", "Sleeping Bag", "LED TV", "Coffee Table",
    "Outdoor Grill", "Espresso Machine", "Office Desk", "Air Fryer Oven", "Power Bank",
    "Stand Mixer", "Massage Chair", "Electric Kettle", "Car GPS", "Portable Speaker",
    "Smart Thermostat", "Smart Doorbell", "Digital Photo Frame", "Car Charger", "Bluetooth Earphones",
    "Wireless Charger", "Desk Lamp", "Fitness Band", "Action Camera", "Gaming Mouse",
    "Office Chair", "Electric Blanket", "Humidifier", "Smart Door Lock", "Hair Straightener",
    "Curling Iron", "Steam Iron", "Cordless Phone", "External SSD", "Digital Drawing Tablet",
    "Noise-Canceling Headphones", "Karaoke Machine", "Baby Monitor", "Air Humidifier", "Car Freshener",
    "USB Flash Drive", "Wireless Keyboard", "LED Desk Lamp", "Computer Monitor", "Smart Light Bulbs",
    "Graphic Tablet", "Wireless Router", "Robot Lawn Mower", "Solar Charger", "Bluetooth Mouse",
    "Coffee Thermos", "Outdoor Speakers", "Car Jump Starter", "Shower Head", "Fitness Treadmill",
    "Smart Mirror", "Smart Scale", "Air Mattress", "Steam Mop", "Back Massager Pillow",
    "Television Stand", "Projector Screen", "Electric Fan", "Memory Foam Pillow", "Air Quality Monitor",
    "Gaming Headset", "Video Doorbell", "Portable Blender", "Digital Voice Recorder", "Car Vacuum Cleaner",
    "Handheld Massager", "Smart Plugs", "Smart Home Hub", "Sleep Tracker", "Wireless Security Camera",
    "Smart Watch Charger", "Gaming Chair", "Digital Alarm Clock", "Smart Refrigerator", "Water Flosser",
    "Fitness Gloves", "Cordless Screwdriver", "Wireless Gaming Mouse", "Car Seat Organizer", "Bluetooth Car Kit",
    "Electric Scooter", "Smart Water Bottle", "Mini Projector", "Indoor Bike Trainer", "Gaming Keyboard",
    "Portable Grill", "Hand Warmer", "Mini Fridge", "Indoor Security Camera", "Cordless Hair Dryer",
    "Electric Skillet", "Coffee Warmer", "Wireless Barcode Scanner", "Smart Home Thermostat", "Robot Window Cleaner",
    "Smart Air Purifier", "Smart Humidifier", "Gaming Desk", "Digital TV Antenna", "Indoor Bike",
    "Wireless HDMI Transmitter", "Digital Meat Thermometer", "Sleep Headphones", "Smart Air Fryer", "Wireless Charging Pad",
    "Gaming Console Stand", "Wireless Presenter", "Solar Powered Charger", "Portable Espresso Maker", "Smart Fitness Mat",
    "Indoor Plant Stand", "Gaming Laptop Cooler", "Wireless Car Charger", "Smart Pet Feeder", "Smart Mirror Scale",
    "Digital Luggage Scale", "Portable Power Station", "Smart Backpack", "Smart Door Viewer", "Electric Bike",
    "Wireless Bike Computer", "Gaming Desk Chair", "Smart Curtain Rod", "Smart Wine Opener", "Smart Pet Collar",
    "Wireless Gaming Controller", "Digital Laser Tape Measure", "Smart LED Strip Lights", "Smart Glasses", "Smart Bed Frame",
    "Wireless Meat Thermometer", "Smart Kitchen Scale", "Digital Refrigerator Thermometer", "Smart Ceiling Fan", "Smart Sleep Aid",
    "Portable Ice Maker", "Gaming Mouse Pad", "Digital Drawing Pen", "Smart Neck Massager", "Smart Water Leak Detector",
    "Gaming Desk Accessories", "Wireless Book Light", "Smart Air Quality Monitor", "Smart Coffee Grinder", "Wireless Meat Smoker",
    "Digital Food Thermometer", "Smart Light Switch", "Smart Lawn Mower", "Smart Plant Watering System", "Smart Desk Organizer",
    "Gaming Console Organizer", "Wireless Video Doorbell", "Digital Video Baby Monitor", "Wireless Ergonomic Mouse", "Wireless HDMI Adapter",
    "Smart Wall Charger", "Digital Water Thermometer", "Smart Clothes Steamer", "Wireless Digital Microscope", "Smart Outdoor Camera",
    "Smart Electric Toothbrush", "Wireless Smart Doorbell", "Digital Baby Monitor", "Smart Rice Cooker", "Gaming Console Shelf",
    "Wireless Bluetooth Adapter", "Smart Outdoor Lights", "Smart Umbrella", "Digital Kitchen Scale", "Wireless Bluetooth Earbuds",
    "Gaming Console Storage", "Smart Refrigerator Organizer", "Wireless Digital Notepad", "Smart Hand Warmer", "Digital Soil Moisture Meter",
    "Wireless Grill Thermometer", "Smart Pet Door", "Digital pH Meter", "Wireless Grill Brush", "Smart Portable Printer",
    "Wireless Electric Blanket", "Smart Desk Fan", "Smart Watering Can", "Digital Wind Speed Meter", "Wireless Floating Pool Speaker",
    "Smart Light Bulb Socket", "Digital Pool Thermometer", "Wireless Digital Photo Frame", "Smart Cup Warmer", "Wireless Digital Hygrometer",
    "Digital Barbecue Thermometer", "Smart Plant Pot", "Wireless Smart Plugs", "Digital Rain Gauge", "Smart Garage Door Opener",
    "Wireless Pool Thermometer", "Digital Hydration Reminder", "Smart Pool Thermometer", "Wireless Digital Microphone", "Smart Watering Hose",
    "Digital Pool pH Meter", "Wireless Digital Fishing Scale", "Smart Lawn Sprinkler", "Digital Bird Feeder", "Wireless Smart Mirror",
    "Smart Fire Pit", "Wireless Digital Breathalyzer", "Smart Pool Cover", "Digital Smart Pen", "Wireless Digital Tire Pressure Gauge",
    "Smart Garden Watering System", "Wireless Digital Level", "Smart Outdoor Heater", "Digital Smart Glasses", "Wireless Digital Laser Tape Measure",
    "Smart Outdoor Blinds", "Wireless Digital Stud Finder", "Smart Outdoor Umbrella", "Digital Smart Refrigerator", "Wireless Digital Light Meter",
    "Smart Outdoor Projector", "Wireless Digital Moisture Meter", "Smart Outdoor Sound System", "Wireless Digital Inspection Camera", "Smart Outdoor Grill",
    "Wireless Digital Voltage Tester", "Smart Outdoor Furniture", "Digital Smart Dog Collar", "Wireless Digital Water Quality Tester", "Smart Outdoor Security Camera",
    "Wireless Digital Soil pH Meter", "Smart Outdoor Ceiling Fan", "Digital Smart Bike Lock", "Wireless Digital Food Thermometer", "Smart Outdoor Wall Light",
    "Wireless Digital Doorbell", "Smart Outdoor Planter", "Digital Smart BBQ Grill", "Wireless Digital Ear Thermometer", "Smart Outdoor Solar Lights",
    "Wireless Digital Indoor Thermometer", "Digital Smart Home Lock", "Wireless Digital Wind Speed Meter", "Smart Outdoor String Lights", "Wireless Digital Light Switch",
    "Digital Smart Bird Feeder", "Wireless Digital Wall Clock", "Smart Outdoor Mosquito Repellent", "Wireless Digital Air Quality Monitor", "Smart Outdoor Water Fountain",
    "Wireless Digital Smart Mirror", "Digital Smart Weather Station", "Wireless Digital Touchpad", "Smart Outdoor Ice Maker", "Wireless Digital Dog Collar",
    "Digital Smart Pet Door", "Wireless Digital Cat Feeder", "Smart Outdoor Fire Pit", "Wireless Digital Aquarium Thermometer", "Smart Outdoor Bluetooth Speaker",
    "Wireless Digital Aquarium Heater", "Smart Outdoor Solar Fountain", "Wireless Digital Aquarium Filter", "Digital Smart Fish Tank", "Wireless Digital Aquarium Light",
    "Smart Outdoor Solar Charger", "Wireless Digital Aquarium Pump", "Digital Smart Fish Feeder", "Wireless Digital Aquarium Water Heater", "Smart Outdoor Solar Lantern",
    "Wireless Digital Aquarium Heater Controller", "Digital Smart Aquarium", "Wireless Digital Aquarium Temperature Controller", "Smart Outdoor Solar String Lights", "Wireless Digital Aquarium Water Pump",
]

# List of Canadian stores
canadian_stores = [
    "Loblaws", "Walmart", "Sobeys", "Costco", "Metro",
    "Shoppers Drug Mart", "Canadian Tire", "No Frills",
    "Superstore", "Rexall", "Dollarama", "Home Hardware"
]

# Create a workbook and add a sheet
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Product Store Mapping"

# Add headers to the sheet
sheet["A1"] = "Item Name"
sheet["B1"] = "Store"

# Shuffle the list of products
random.shuffle(product_names)

# Create a dictionary to store product-store mappings
product_store_mapping = {}

# Assign each product to a store
for row, product in enumerate(product_names, start=2):
    # Choose a random store for the product
    chosen_store = random.choice(canadian_stores)

    # Assign the product to the chosen store
    product_store_mapping[product] = chosen_store

    # Write data to the sheet
    sheet[f"A{row}"] = product
    sheet[f"B{row}"] = chosen_store

# Save the workbook to a file
workbook.save("product_store_mapping.xlsx")
