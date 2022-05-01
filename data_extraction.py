def get_title(item_tag):
    title = item_tag \
        .find("span", {"class": "product-title"}) \
        .find("span") \
        .text.strip()
    return title

def get_description(item_tag):
    description = item_tag \
        .find("p", {"class": "product-subtitle"}) \
        .text.strip()
    return description

def get_image(item_tag):
    image = item_tag \
        .find("img")["src"]
    return image

def get_price(item_tag):
    price = item_tag.find("span", {"class": "price-line"}) 
    if price is not None:
        price = price.text.strip()
        price = price.replace("Dès ", "")
        price = price.split("€")[0]
        price = price.replace(",", ".")
    else:
        price = None
    return price