import json
import random
import linecache
import pandas as pd

def read_file(filename, category):
    num_lines = sum(1 for line in open(filename))
    selected_lines = set()
    while len(selected_lines) < min(1000, num_lines):
        line_num = random.randint(1, num_lines)
        if line_num not in selected_lines:
            selected_lines.add(line_num)
            line = linecache.getline(filename, line_num)
            selected_data = json.loads(line)
            selected_data['category'] = category
            yield selected_data

data = []

# load each file and join into dataframe
for category, filename in [('arts_crafts_and_sewing', "/Users/pavansingh/Desktop/Amazon Review Data/Electronics_5.json"), ('automotive', "/Users/pavansingh/Desktop/Amazon Review Data/Automotive_5.json"), ('cds_vinyl', "/Users/pavansingh/Desktop/Amazon Review Data/CDs_and_Vinyl_5.json"), ('cell_phones', "/Users/pavansingh/Desktop/Amazon Review Data/Cell_Phones_and_Accessories_5.json"), ('clothing_shoes', "/Users/pavansingh/Desktop/Amazon Review Data/Clothing_Shoes_and_Jewelry_5.json"), ('electronics', "/Users/pavansingh/Desktop/Amazon Review Data/Electronics_5.json"), ('grocery', "/Users/pavansingh/Desktop/Amazon Review Data/Grocery_and_Gourmet_Food_5.json"), ('home_kitchen', "/Users/pavansingh/Desktop/Amazon Review Data/Home_and_Kitchen_5.json"), ('kindle_store', "/Users/pavansingh/Desktop/Amazon Review Data/Kindle_Store_5.json"), ('movies_tv', "/Users/pavansingh/Desktop/Amazon Review Data/Movies_and_TV_5.json"), ('musical_instruments', "/Users/pavansingh/Desktop/Amazon Review Data/Musical_Instruments_5.json"), ('office_products', "/Users/pavansingh/Desktop/Amazon Review Data/Office_Products_5.json"), ('patio_lawn', "/Users/pavansingh/Desktop/Amazon Review Data/Patio_Lawn_and_Garden_5.json"), ('pet_supplies', "/Users/pavansingh/Desktop/Amazon Review Data/Pet_Supplies_5.json"), ('sports_outdoors', "/Users/pavansingh/Desktop/Amazon Review Data/Sports_and_Outdoors_5.json"), ('tools_home', "/Users/pavansingh/Desktop/Amazon Review Data/Tools_and_Home_Improvement_5.json"), ('toys_games', "/Users/pavansingh/Desktop/Amazon Review Data/Toys_and_Games_5.json"), ('video_games', "/Users/pavansingh/Desktop/Amazon Review Data/Video_Games_5.json")]:
    for selected_data in read_file(filename, category):
        data.append(selected_data)
# make it into a dataframe
df = pd.DataFrame(data)

# show the dataframe
print("Shape of all data:", df.shape)
display(df.head(5))

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################


arts_crafts = "/Users/pavansingh/Desktop/Amazon Review Data/Arts_Crafts_and_Sewing_5.json"
arts_crafts = pd.read_json(arts_crafts, lines=True)
arts_crafts['category'] = 'arts_crafts' 
print("Shape of Arts & Crafts: ", arts_crafts.shape)

# take a random sample of size 70000 from the dataset
arts_crafts = arts_crafts.sample(n=70000, random_state=1)
print("Shape of Arts & Crafts: ", arts_crafts.shape)

automotive = "/Users/pavansingh/Desktop/Amazon Review Data/Automotive_5.json"
automotive = pd.read_json(automotive, lines=True)
automotive['category'] = 'automotive'
print("Shape of Automotive: ", automotive.shape)

# take a random sample of size 70000 from the dataset
automotive = automotive.sample(n=70000, random_state=1)
print("Shape of Automotive: ", automotive.shape)

cds_vinyl = "/Users/pavansingh/Desktop/Amazon Review Data/CDs_and_Vinyl_5.json"
cds_vinyl = pd.read_json(cds_vinyl, lines=True)
cds_vinyl['category'] = 'cds_vinyl'
print("Shape of CDs & Vinyl: ", cds_vinyl.shape)

# take a random sample of size 70000 from the dataset
cds_vinyl = cds_vinyl.sample(n=70000, random_state=1)
print("Shape of CDs & Vinyl: ", cds_vinyl.shape)

#read in the cell phones dataset but only take 70000 rows


cell_phones = "/Users/pavansingh/Desktop/Amazon Review Data/Cell_Phones_and_Accessories_5.json"
cell_phones = pd.read_json(cell_phones, lines=True)
cell_phones['category'] = 'cell_phones'
print("Shape of Cell Phones: ", cell_phones.shape)

# take a random sample of size 70000 from the dataset
cell_phones = cell_phones.sample(n=70000, random_state=1)
print("Shape of Cell Phones: ", cell_phones.shape)


clothing_shoes = "/Users/pavansingh/Desktop/Amazon Review Data/Clothing_Shoes_and_Jewelry_5.json"
clothing_shoes = pd.read_json(clothing_shoes, lines=True)
clothing_shoes['category'] = 'clothing_shoes'
print("Shape of Clothing & Shoes: ", clothing_shoes.shape)

# take a random sample of size 70000 from the dataset
clothing_shoes = clothing_shoes.sample(n=70000, random_state=1)
print("Shape of Clothing: ", clothing_shoes.shape)
digital_music = "/Users/pavansingh/Desktop/Amazon Review Data/Digital_Music_5.json"
digital_music = pd.read_json(digital_music, lines=True)
digital_music['category'] = 'digital_music'
print("Shape of Digital Music: ", digital_music.shape)
digital_music = digital_music.sample(n=70000, random_state=1)
print("Shape of Digital Music: ", digital_music.shape)

electronics = "/Users/pavansingh/Desktop/Amazon Review Data/Electronics_5.json"
electronics = pd.read_json(electronics, lines=True)
electronics['category'] = 'electronics'
print("Shape of Electronics: ", electronics.shape)
electronics = electronics.sample(n=70000, random_state=1)
print("Shape of Electronics: ", electronics.shape)

grocery_gourmet = "/Users/pavansingh/Desktop/Amazon Review Data/Grocery_and_Gourmet_Food_5.json"
grocery_gourmet = pd.read_json(grocery_gourmet, lines=True)
grocery_gourmet['category'] = 'grocery_gourmet'
print("Shape of Grocery & Gourmet: ", grocery_gourmet.shape)
grocery_gourmet = grocery_gourmet.sample(n=70000, random_state=1)
print("Shape of Grocery & Gourmet: ", grocery_gourmet.shape)


home_kitchen = "/Users/pavansingh/Desktop/Amazon Review Data/Home_and_Kitchen_5.json"
home_kitchen = pd.read_json(home_kitchen, lines=True)
home_kitchen['category'] = 'home_kitchen'
print("Shape of Home & Kitchen: ", home_kitchen.shape)
home_kitchen = home_kitchen.sample(n=70000, random_state=1)
print("Shape of Home & Kitchen: ", home_kitchen.shape)

kindle_store = "/Users/pavansingh/Desktop/Amazon Review Data/Kindle_Store_5.json"
kindle_store = pd.read_json(kindle_store, lines=True)
kindle_store['category'] = 'kindle_store'
print("Shape of Kindle Store: ", kindle_store.shape)
kindle_store = kindle_store.sample(n=70000, random_state=1)
print("Shape of Kindle Store: ", kindle_store.shape)

movies_tv = "/Users/pavansingh/Desktop/Amazon Review Data/Movies_and_TV_5.json"
movies_tv = pd.read_json(movies_tv, lines=True)
movies_tv['category'] = 'movies_tv'
print("Shape of Movies & TV: ", movies_tv.shape)
movies_tv = movies_tv.sample(n=70000, random_state=1)
print("Shape of Movies & TV: ", movies_tv.shape)

musical_instruments = "/Users/pavansingh/Desktop/Amazon Review Data/Musical_Instruments_5.json"
musical_instruments = pd.read_json(musical_instruments, lines=True)
musical_instruments['category'] = 'musical_instruments'
print("Shape of Musical Instruments: ", musical_instruments.shape)
musical_instruments = musical_instruments.sample(n=70000, random_state=1)
print("Shape of Musical Instruments: ", musical_instruments.shape)

office_products = "/Users/pavansingh/Desktop/Amazon Review Data/Office_Products_5.json"
office_products = pd.read_json(office_products, lines=True)
office_products['category'] = 'office_products'
print("Shape of Office Products: ", office_products.shape)
office_products = office_products.sample(n=70000, random_state=1)
print("Shape of Office Products: ", office_products.shape)

patio_lawn = "/Users/pavansingh/Desktop/Amazon Review Data/Patio_Lawn_and_Garden_5.json"
patio_lawn = pd.read_json(patio_lawn, lines=True)
patio_lawn['category'] = 'patio_lawn'
print("Shape of Patio Lawn: ", patio_lawn.shape)
patio_lawn = patio_lawn.sample(n=70000, random_state=1)
print("Shape of Patio Lawn: ", patio_lawn.shape)

pet_supplies = "/Users/pavansingh/Desktop/Amazon Review Data/Pet_Supplies_5.json"
pet_supplies = pd.read_json(pet_supplies, lines=True)
pet_supplies['category'] = 'pet_supplies'
print("Shape of Pet Supplies: ", pet_supplies.shape)
pet_supplies = pet_supplies.sample(n=70000, random_state=1)
print("Shape of Pet Supplies: ", pet_supplies.shape)

prime_pantry = "/Users/pavansingh/Desktop/Amazon Review Data/Prime_Pantry_5.json"
prime_pantry = pd.read_json(prime_pantry, lines=True)
prime_pantry['category'] = 'prime_pantry'
print("Shape of Prime Pantry: ", prime_pantry.shape)
prime_pantry = prime_pantry.sample(n=70000, random_state=1)
print("Shape of Prime Pantry: ", prime_pantry.shape)

sports_outdoors = "/Users/pavansingh/Desktop/Amazon Review Data/Sports_and_Outdoors_5.json"
sports_outdoors = pd.read_json(sports_outdoors, lines=True)
sports_outdoors['category'] = 'sports_outdoors'
print("Shape of Sports & Outdoors: ", sports_outdoors.shape)
sports_outdoors = sports_outdoors.sample(n=70000, random_state=1)
print("Shape of Sports & Outdoors: ", sports_outdoors.shape)

tools_home = "/Users/pavansingh/Desktop/Amazon Review Data/Tools_and_Home_Improvement_5.json"
tools_home = pd.read_json(tools_home, lines=True)
tools_home['category'] = 'tools_home'
print("Shape of Tools & Home: ", tools_home.shape)
tools_home = tools_home.sample(n=70000, random_state=1)
print("Shape of Tools & Home: ", tools_home.shape)

toys_games = "/Users/pavansingh/Desktop/Amazon Review Data/Toys_and_Games_5.json"
toys_games = pd.read_json(toys_games, lines=True)
toys_games['category'] = 'toys_games'
print("Shape of Toys & Games: ", toys_games.shape)
toys_games = toys_games.sample(n=70000, random_state=1)
print("Shape of Toys & Games: ", toys_games.shape)

video_games = "/Users/pavansingh/Desktop/Amazon Review Data/Video_Games_5.json"
video_games = pd.read_json(video_games, lines=True)
video_games['category'] = 'video_games'
print("Shape of Video Games: ", video_games.shape)
video_games = video_games.sample(n=70000, random_state=1)
print("Shape of Video Games: ", video_games.shape)
# combine all data data
all_data = pd.concat([beauty, fashion, appliances, arts_crafts, automotive, books, cds_vinyl, cell_phones, clothing_shoes, digital_music, electronics, gift_cards, grocery_gourmet, home_kitchen, industrial, kindle_store, luxury_beauty, magazine_subscriptions, movies_tv, musical_instruments, office_products, patio_lawn, pet_supplies, prime_pantry, software, sports_outdoors, tools_home, toys_games, video_games], ignore_index = True)

# shape of combined
print("Shape of Combined Data: ", all_data.shape)


books = "/Users/pavansingh/Desktop/Amazon Review Data/Books_5.json"
books = pd.read_json(books, lines=True)
books['category'] = 'books'
print("Shape of Books: ", books.shape)





# # load all the datasets into env

# beauty = "/Users/pavansingh/Desktop/Amazon Review Data/All_Beauty_5.json"
# beauty = pd.read_json(beauty, lines=True)
# beauty['category'] = 'beauty'
# print("Shape of Beauty: ", beauty.shape)

# fashion = "/Users/pavansingh/Desktop/Amazon Review Data/AMAZON_FASHION_5.json"
# fashion = pd.read_json(fashion, lines=True)
# fashion['category'] = 'fashion'
# print("Shape of Fashion: ", fashion.shape)

# appliances = "/Users/pavansingh/Desktop/Amazon Review Data/Appliances_5.json"
# appliances = pd.read_json(appliances, lines=True)
# appliances['category'] = 'appliances'
# print("Shape of Appliances: ", appliances.shape)

# gift_cards = "/Users/pavansingh/Desktop/Amazon Review Data/Gift_Cards_5.json"
# gift_cards = pd.read_json(gift_cards, lines=True)
# gift_cards['category'] = 'gift_cards'
# print("Shape of Gift Cards: ", gift_cards.shape)

# industrial = "/Users/pavansingh/Desktop/Amazon Review Data/Industrial_and_Scientific_5.json"
# industrial = pd.read_json(industrial, lines=True)
# industrial['category'] = 'industrial'
# print("Shape of Industrial: ", industrial.shape)


# luxury_beauty = "/Users/pavansingh/Desktop/Amazon Review Data/Luxury_Beauty_5.json"
# luxury_beauty = pd.read_json(luxury_beauty, lines=True)
# luxury_beauty['category'] = 'luxury_beauty'
# print("Shape of Luxury Beauty: ", luxury_beauty.shape)

# magazine_subscriptions = "/Users/pavansingh/Desktop/Amazon Review Data/Magazine_Subscriptions_5.json"
# magazine_subscriptions = pd.read_json(magazine_subscriptions, lines=True)
# magazine_subscriptions['category'] = 'magazine_subscriptions'
# print("Shape of Magazine Subscriptions: ", magazine_subscriptions.shape)

# software = "/Users/pavansingh/Desktop/Amazon Review Data/Software_5.json"
# software = pd.read_json(software, lines=True)
# software['category'] = 'software'
# print("Shape of Software: ", software.shape)

# # merge the smaller datasets into one dataframe
# # combine all data data
# all_data = pd.concat([beauty, fashion, appliances, gift_cards, industrial, luxury_beauty, magazine_subscriptions, software], ignore_index = True)

# # shape of combined data
# print("Shape of Combined Data: ", all_data.shape)
# display(all_data)



# read smaller reviews

# category files - large reviews
cds_vinyl = "/Users/pavansingh/Desktop/Amazon Review Data/CDs_and_Vinyl_5.json"
cell_phones = "/Users/pavansingh/Desktop/Amazon Review Data/Cell_Phones_and_Accessories_5.json"
clothing_shoes = "/Users/pavansingh/Desktop/Amazon Review Data/Clothing_Shoes_and_Jewelry_5.json"
electronics = "/Users/pavansingh/Desktop/Amazon Review Data/Electronics_5.json"
grocery = "/Users/pavansingh/Desktop/Amazon Review Data/Grocery_and_Gourmet_Food_5.json"
home_kitchen = "/Users/pavansingh/Desktop/Amazon Review Data/Home_and_Kitchen_5.json"
kindle_store = "/Users/pavansingh/Desktop/Amazon Review Data/Kindle_Store_5.json"
movies_tv = "/Users/pavansingh/Desktop/Amazon Review Data/Movies_and_TV_5.json"
musical_instruments = "/Users/pavansingh/Desktop/Amazon Review Data/Musical_Instruments_5.json"
office_products = "/Users/pavansingh/Desktop/Amazon Review Data/Office_Products_5.json"
prime_pantry = "/Users/pavansingh/Desktop/Amazon Review Data/Prime_Pantry_5.json"
patio_lawn = "/Users/pavansingh/Desktop/Amazon Review Data/Patio_Lawn_and_Garden_5.json"
pet_supplies = "/Users/pavansingh/Desktop/Amazon Review Data/Pet_Supplies_5.json"
sports_outdoors = "/Users/pavansingh/Desktop/Amazon Review Data/Sports_and_Outdoors_5.json"
tools_home = "/Users/pavansingh/Desktop/Amazon Review Data/Tools_and_Home_Improvement_5.json"
toys_games = "/Users/pavansingh/Desktop/Amazon Review Data/Toys_and_Games_5.json"
video_games = "/Users/pavansingh/Desktop/Amazon Review Data/Video_Games_5.json"

# load each file and join into dataframe
for category, filename in [('arts_crafts_and_sewing', arts_crafts), ('automotive', automotive), ('cds_and_vinyl', cds_vinyl), ('cell_phones_and_accessories', cell_phones), ('clothing_shoes', clothing_shoes), ('electronics', electronics), ('grocery', grocery), ('home_and_kitchen', home_kitchen),  ('kindle_store', kindle_store), ('movies_tv', movies_tv), ('musical_instruments', musical_instruments), ('office_products', office_products),  ('patio_lawn', patio_lawn), ('pet_supplies', pet_supplies), ('sports_outdoors', sports_outdoors), ('tools_and_home_improvement', tools_home), ('toys_and_games', toys_games), ('video_games', video_games)]:
    for selected_data in read_file(filename, category):
        data.append(selected_data)

# make it into a dataframe
data_with_large_reviews = pd.DataFrame(data)

# show the dataframe
print("Shape of Data with Large Reviews Merged:", data_with_large_reviews.shape)
display(data_with_large_reviews.head(5))

# save df to csv called lots_revs.csv
data_with_large_reviews.to_csv('lots_revs.csv')

# category value counts
print("Value counts of product reviews per category:\n",data_with_large_reviews['category'].value_counts())










# get index of top 6 products with highest and lowest sentiment averages
top6_prod_afinn = prod_data.sort_values(['mean_sent_afinn'], ascending=False).index[0:5] # TOP 6 products with highest sentiment average - afinn

low_6_prod_afinn = prod_data.sort_values(['mean_sent_afinn'], ascending=True).index[0:5] # BOTTOM 6 products with lowest sentiment average - afinn

top6_prod_bing = prod_data.sort_values(['mean_sent_bing'], ascending=False).index[0:5] # TOP 6 products with highest sentiment average - bing

low_6_prod_bing = prod_data.sort_values(['mean_sent_bing'], ascending=True).index[0:5] # BOTTOM 6 products with lowest sentiment average - bing

top6_prod_textblob = prod_data.sort_values(['mean_sent_textblob'], ascending=False).index[0:5] # TOP 6 products with highest sentiment average - textblob

low_6_prod_textblob = prod_data.sort_values(['mean_sent_textblob'], ascending=True).index[0:5] # BOTTOM 6 products with lowest sentiment average - textblob


# get all rows for product index 
top6_prod_afinn_data = data_sentiments[data_sentiments['asin'].isin(top6_prod_afinn)]
low_6_prod_afinn_data = data_sentiments[data_sentiments['asin'].isin(low_6_prod_afinn)]
top6_prod_bing_data = data_sentiments[data_sentiments['asin'].isin(top6_prod_bing)]
low_6_prod_bing_data = data_sentiments[data_sentiments['asin'].isin(low_6_prod_bing)]
top6_prod_textblob_data = data_sentiments[data_sentiments['asin'].isin(top6_prod_textblob)]
low_6_prod_textblob_data = data_sentiments[data_sentiments['asin'].isin(low_6_prod_textblob)]



fig = plt.figure(figsize=(20, 14))
fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.1, hspace=0.4)


# AFINN
# plot a violin plot for each product in prod_afinn_data using seaborn for sentiment afinn 
plt.subplot(3, 2, 1)
sns.violinplot(x="asin", y="sentiment_score_afinn_revText", data=top6_prod_afinn_data, palette="Set3", linewidth=1, inner="quartile")
plt.title("Sentiment Distribution (Positive) - AFINN", fontsize=20, fontweight='bold')
plt.xlabel("Product", fontsize=12, fontweight='semibold')
plt.ylabel("Sentiment", fontsize=12, fontweight='semibold')
plt.xticks(rotation=45)


plt.subplot(3, 2, 3)
sns.violinplot(x="asin", y="sentiment_score_afinn_revText", data=low_6_prod_afinn_data, palette="Set3", linewidth=1, inner="quartile")
plt.title("Sentiment Distribution (Negative) - AFINN", fontsize=20, fontweight='bold')
plt.xlabel("Product", fontsize=12, fontweight='semibold')
plt.ylabel("Sentiment", fontsize=12, fontweight='semibold')
plt.xticks(rotation=45)


# BING
# plot a violin plot for each product in prod_bing_data using seaborn for sentiment bing
plt.subplot(3, 2, 2)
sns.violinplot(x="asin", y="sentiment_score_bing_revText", data=top6_prod_bing_data, palette="Set3", linewidth=1, inner="quartile")
plt.title("Sentiment Distribution (Positive) - BING", fontsize=20, fontweight='bold')
plt.xlabel("Product", fontsize=12, fontweight='semibold')
plt.ylabel("Sentiment", fontsize=12, fontweight='semibold')
plt.xticks(rotation=45)

plt.subplot(3, 2, 4)
sns.violinplot(x="asin", y="sentiment_score_bing_revText", data=low_6_prod_bing_data, palette="Set3", linewidth=1, inner="quartile")
plt.title("Sentiment Distribution (Negative) - BING", fontsize=20, fontweight='bold')
plt.xlabel("Product", fontsize=12, fontweight='semibold')
plt.ylabel("Sentiment", fontsize=12, fontweight='semibold')
plt.xticks(rotation=45)

# TEXTBLOB
# plot a violin plot for each product in prod_textblob_data using seaborn for sentiment textblob
plt.subplot(3, 2, 5)
sns.violinplot(x="asin", y="sentiments_textblob_revText", data=top6_prod_textblob_data, palette="Set3", linewidth=1, inner="quartile")
plt.title("Sentiment Distribution (Positive) - TEXTBLOB", fontsize=20, fontweight='bold')
plt.xlabel("Product", fontsize=12, fontweight='semibold')
plt.ylabel("Sentiment", fontsize=12, fontweight='semibold')
plt.xticks(rotation=45)

plt.subplot(3, 2, 6)
sns.violinplot(x="asin", y="sentiments_textblob_revText", data=low_6_prod_textblob_data, palette="Set3", linewidth=1, inner="quartile")
plt.title("Sentiment Distribution (Negative) - TEXTBLOB", fontsize=20, fontweight='bold')
plt.xlabel("Product", fontsize=12, fontweight='semibold')
plt.ylabel("Sentiment", fontsize=12, fontweight='semibold')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

