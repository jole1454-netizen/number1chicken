import streamlit as st
from datetime import datetime
import textwrap

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Number 1 Chicken",
    page_icon="🍗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS - RESPONSIVE FOR PHONE / TABLET / PC
# ============================================================
st.markdown(textwrap.dedent("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap');
* {
    font-family: 'Montserrat', sans-serif;
    box-sizing: border-box;
}
html, body {
    margin: 0;
    padding: 0;
    overflow-x: hidden;
}
.stApp {
    background: #f5f5f5;
}
/* Main container */
.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
    padding-left: 4%;
    padding-right: 4%;
    padding-bottom: 3rem;
}
/* Sidebar */
section[data-testid="stSidebar"] {
    background: #111111;
}
section[data-testid="stSidebar"] * {
    color: white !important;
}
/* Brand */
.brand-box {
    text-align: center;
    padding: 10px 0 20px 0;
}
.brand-main {
    color: #e21d2d;
    font-size: 28px;
    font-weight: 900;
}
.brand-sub {
    color: white;
    font-size: 10px;
    letter-spacing: 4px;
}
/* Hero */
.hero {
    width: 100%;
    min-height: 380px;
    border-radius: 25px;
    padding: 55px;
    margin-bottom: 30px;
    background:
        linear-gradient(
            90deg,
            rgba(0,0,0,0.92),
            rgba(0,0,0,0.55),
            rgba(220,29,45,0.65)
        ),
        url("https://images.unsplash.com/photo-1513639776629-7b61b0ac49cb");
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
}
.hero-content {
    max-width: 700px;
}
.hero-small {
    color: #ff5252;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 12px;
}
.hero-title {
    color: white;
    font-size: 58px;
    line-height: 1;
    font-weight: 900;
    margin-bottom: 20px;
}
.hero-text {
    color: #eeeeee;
    font-size: 16px;
    line-height: 1.7;
}
/* Sections */
.section-title {
    font-size: 32px;
    font-weight: 900;
    color: #181818;
    margin-top: 35px;
}
.section-subtitle {
    color: #777777;
    margin-bottom: 25px;
}
/* Product card */
.product-card {
    background: white;
    border-radius: 20px;
    padding: 15px;
    margin-bottom: 20px;
    border: 1px solid #eeeeee;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
    overflow: hidden;
}
.product-card img {
    width: 100%;
    border-radius: 15px;
}
.product-name {
    color: #181818;
    font-size: 18px;
    font-weight: 800;
    margin-top: 12px;
}
.product-category {
    color: #999999;
    text-transform: uppercase;
    font-size: 11px;
    letter-spacing: 1px;
    margin-top: 4px;
}
.product-description {
    color: #666666;
    font-size: 13px;
    line-height: 1.5;
    min-height: 40px;
    margin-top: 8px;
}
.product-price {
    color: #e21d2d;
    font-size: 20px;
    font-weight: 900;
    margin: 12px 0;
}
/* Buttons */
.stButton > button {
    width: 100%;
    min-height: 44px;
    border: 0;
    border-radius: 12px;
    background: #e21d2d;
    color: white;
    font-weight: 800;
}
.stButton > button:hover {
    background: #b91421;
    color: white;
}
/* Stats */
.stat-card {
    background: white;
    border-radius: 18px;
    padding: 20px 10px;
    text-align: center;
    box-shadow: 0 4px 18px rgba(0,0,0,0.05);
}
.stat-number {
    color: #e21d2d;
    font-size: 28px;
    font-weight: 900;
}
.stat-label {
    color: #777777;
    font-size: 12px;
}
/* Promo */
.promo {
    background: #fff0f1;
    border: 1px solid #ffd2d5;
    border-radius: 20px;
    padding: 25px;
    margin: 30px 0;
}
.promo-title {
    color: #e21d2d;
    font-size: 22px;
    font-weight: 900;
}
/* Cart */
.cart-item {
    background: white;
    padding: 18px;
    border-radius: 18px;
    margin-bottom: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}
.cart-total {
    background: #151515;
    color: white;
    padding: 25px;
    border-radius: 18px;
    margin: 20px 0;
}
.total-price {
    color: #ff3949;
    font-size: 30px;
    font-weight: 900;
}
/* Footer */
.footer {
    background: #111111;
    color: #aaaaaa;
    text-align: center;
    border-radius: 20px;
    padding: 30px;
    margin-top: 60px;
}
.footer-title {
    color: #e21d2d;
    font-size: 25px;
    font-weight: 900;
}
/* ========================================================
   PHONE
   ======================================================== */
@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1rem;
    }
    .hero {
        min-height: 430px;
        padding: 30px 22px;
        border-radius: 20px;
        background-position: center;
    }
    .hero-title {
        font-size: 38px;
        line-height: 1.05;
    }
    .hero-text {
        font-size: 14px;
    }
    .hero-small {
        font-size: 11px;
        letter-spacing: 2px;
    }
    .section-title {
        font-size: 27px;
    }
    .product-name {
        font-size: 17px;
    }
    .product-price {
        font-size: 18px;
    }
    .stat-card {
        margin-bottom: 10px;
    }
    .promo {
        padding: 20px;
    }
    .footer {
        padding: 25px 15px;
    }
}
/* ========================================================
   SMALL PHONE
   ======================================================== */
@media (max-width: 480px) {
    .block-container {
        padding-left: 0.7rem;
        padding-right: 0.7rem;
    }
    .hero {
        min-height: 400px;
        padding: 25px 18px;
    }
    .hero-title {
        font-size: 31px;
    }
    .hero-text {
        font-size: 13px;
    }
    .section-title {
        font-size: 24px;
    }
    .product-card {
        padding: 12px;
        border-radius: 16px;
    }
    .product-description {
        font-size: 12px;
    }
    .stButton > button {
        min-height: 46px;
    }
}
</style>
"""), unsafe_allow_html=True)

# ============================================================
# PRODUCTS
# ============================================================
PRODUCTS = [
    {
        "id": 1,
        "name": "Crispy Chicken",
        "category": "Chicken",
        "price": 18000,
        "description": "Golden crispy chicken with our signature seasoning.",
        "image": "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec"
    },
    {
        "id": 2,
        "name": "Spicy Chicken",
        "category": "Chicken",
        "price": 20000,
        "description": "Crispy chicken with a delicious spicy coating.",
        "image": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec"
    },
    {
        "id": 3,
        "name": "Chicken Burger",
        "category": "Burger",
        "price": 28000,
        "description": "Crispy chicken fillet with lettuce and special sauce.",
        "image": "https://images.unsplash.com/photo-1615297928064-24977384d0da"
    },
    {
        "id": 4,
        "name": "Beef Burger",
        "category": "Burger",
        "price": 32000,
        "description": "Juicy beef patty with cheese and signature sauce.",
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"
    },
    {
        "id": 5,
        "name": "Chicken Rice",
        "category": "Meals",
        "price": 26000,
        "description": "Crispy chicken served with warm seasoned rice.",
        "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd"
    },
    {
        "id": 6,
        "name": "Chicken Combo",
        "category": "Combo",
        "price": 38000,
        "description": "Chicken, fries and refreshing drink.",
        "image": "https://images.unsplash.com/photo-1600891964599-f61ba0e24092"
    },
    {
        "id": 7,
        "name": "Family Bucket",
        "category": "Combo",
        "price": 95000,
        "description": "Family-sized bucket packed with crispy chicken.",
        "image": "https://images.unsplash.com/photo-1513639776629-7b61b0ac49cb"
    },
    {
        "id": 8,
        "name": "French Fries",
        "category": "Sides",
        "price": 14000,
        "description": "Crispy golden fries with light seasoning.",
        "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877"
    },
    {
        "id": 9,
        "name": "Cheese Fries",
        "category": "Sides",
        "price": 18000,
        "description": "Golden fries topped with creamy cheese.",
        "image": "https://images.unsplash.com/photo-1639024471283-03518883512d"
    },
    {
        "id": 10,
        "name": "Cola",
        "category": "Drinks",
        "price": 10000,
        "description": "Cold and refreshing cola.",
        "image": "https://images.unsplash.com/photo-1629203851122-3726ecdf080e"
    },
    {
        "id": 11,
        "name": "Iced Tea",
        "category": "Drinks",
        "price": 9000,
        "description": "Fresh sweet iced tea.",
        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc"
    },
    {
        "id": 12,
        "name": "Chocolate Sundae",
        "category": "Dessert",
        "price": 15000,
        "description": "Soft vanilla ice cream with chocolate topping.",
        "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb"
    }
]

# ============================================================
# SESSION STATE
# ============================================================
if "cart" not in st.session_state:
    st.session_state.cart = []

if "orders" not in st.session_state:
    st.session_state.orders = []

# ============================================================
# FUNCTIONS
# ============================================================
def rupiah(number):
    return "Rp" + f"{number:,}".replace(",", ".")


def add_to_cart(product_id):
    product = next(
        (p for p in PRODUCTS if p["id"] == product_id),
        None
    )

    if product is None:
        return

    for item in st.session_state.cart:
        if item["id"] == product_id:
            item["quantity"] += 1
            return

    st.session_state.cart.append({
        "id": product["id"],
        "name": product["name"],
        "price": product["price"],
        "image": product["image"],
        "quantity": 1
    })


def remove_from_cart(product_id):
    st.session_state.cart = [
        item
        for item in st.session_state.cart
        if item["id"] != product_id
    ]


def total_price():
    return sum(
        item["price"] * item["quantity"]
        for item in st.session_state.cart
    )


def total_items():
    return sum(
        item["quantity"]
        for item in st.session_state.cart
    )


def product_card(product):

    st.markdown(
        '<div class="product-card">',
        unsafe_allow_html=True
    )

    st.image(
        product["image"],
        width="stretch"
    )

    st.markdown(
        f'<div class="product-name">{product["name"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="product-category">{product["category"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="product-description">'
        f'{product["description"]}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="product-price">'
        f'{rupiah(product["price"])}'
        f'</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "ADD TO ORDER",
        key=f"add_{product['id']}",
        width="stretch"
    ):
        add_to_cart(product["id"])
        st.toast(
            f"{product['name']} added to cart!"
        )

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:

    st.markdown(textwrap.dedent("""
        <div class="brand-box">
            <div class="brand-main">NUMBER 1</div>
            <div class="brand-sub">CHICKEN</div>
        </div>
        """), unsafe_allow_html=True)

    st.divider()

    page = st.radio(
        "MENU",
        [
            "Home",
            "Menu",
            "Deals",
            "Cart",
            "About"
        ]
    )

    st.divider()

    st.write(f"🛒 {total_items()} item(s)")

# ============================================================
# HOME
# ============================================================
if page == "Home":

    st.markdown(textwrap.dedent("""
        <div class="hero">
            <div class="hero-content">
                <div class="hero-small">
                    NUMBER 1 CHICKEN
                </div>
                <div class="hero-title">
                    CRISPY.<br>
                    JUICY.<br>
                    UNFORGETTABLE.
                </div>
                <div class="hero-text">
                    Crispy chicken, juicy burgers,
                    loaded fries and family meals.
                    Your new favorite fast-food destination.
                </div>
            </div>
        </div>
        """), unsafe_allow_html=True)

    # Statistics
    cols = st.columns(4)

    stats = [
        ("12+", "Menu Items"),
        ("15+", "Stores"),
        ("4.9/5", "Rating"),
        ("100%", "Fresh")
    ]

    for col, data in zip(cols, stats):

        with col:

            st.markdown(
                f"""
                <div class="stat-card">
                    <div class="stat-number">{data[0]}</div>
                    <div class="stat-label">{data[1]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Promo
    st.markdown(textwrap.dedent("""
        <div class="promo">
            <div class="promo-title">
                🔥 FAMILY FEAST
            </div>
            <p>
                Feed the whole family with our delicious
                chicken bucket combo.
            </p>
        </div>
        """), unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Best Sellers</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Customer favorites.'
        '</div>',
        unsafe_allow_html=True
    )

    best = [
        PRODUCTS[0],
        PRODUCTS[2],
        PRODUCTS[5],
        PRODUCTS[6]
    ]

    cols = st.columns(4)

    for col, product in zip(cols, best):

        with col:
            product_card(product)

# ============================================================
# MENU
# ============================================================
elif page == "Menu":

    st.markdown(
        '<div class="section-title">Our Menu</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Fresh food. Big flavor.'
        '</div>',
        unsafe_allow_html=True
    )

    search = st.text_input(
        "Search",
        placeholder="Chicken, burger, fries..."
    )

    categories = [
        "All",
        "Chicken",
        "Burger",
        "Meals",
        "Combo",
        "Sides",
        "Drinks",
        "Dessert"
    ]

    category = st.selectbox(
        "Category",
        categories
    )

    filtered = PRODUCTS.copy()

    if category != "All":

        filtered = [
            p
            for p in filtered
            if p["category"] == category
        ]

    if search.strip():

        keyword = search.lower().strip()

        filtered = [
            p
            for p in filtered
            if keyword in p["name"].lower()
            or keyword in p["category"].lower()
            or keyword in p["description"].lower()
        ]

    if len(filtered) == 0:

        st.warning(
            "No products found. Try another search."
        )

    else:

        # Four columns on PC,
        # Streamlit automatically stacks them on smaller screens.
        for i in range(0, len(filtered), 4):

            row = filtered[i:i + 4]

            cols = st.columns(4)

            for col, product in zip(cols, row):

                with col:
                    product_card(product)

# ============================================================
# DEALS
# ============================================================
elif page == "Deals":

    st.markdown(
        '<div class="section-title">Deals</div>',
        unsafe_allow_html=True
    )

    deals = [
        {
            "id": "deal_lunch",
            "name": "Lunch Box",
            "description": "Chicken + Rice + Drink",
            "price": 32000
        },
        {
            "id": "deal_combo",
            "name": "Chicken Combo",
            "description": "2 Chicken + Fries + Drink",
            "price": 38000
        },
        {
            "id": "deal_family",
            "name": "Family Feast",
            "description": "8 Chicken + 2 Fries + 4 Drinks",
            "price": 119000
        }
    ]

    for i in range(0, len(deals), 3):

        row = deals[i:i + 3]

        cols = st.columns(3)

        for col, deal in zip(cols, row):

            with col:

                st.markdown(
                    f"""
                    <div class="product-card">
                        <div class="hero-small">
                            SPECIAL OFFER
                        </div>

                        <h2>{deal["name"]}</h2>

                        <p>
                            {deal["description"]}
                        </p>

                        <div class="product-price">
                            {rupiah(deal["price"])}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    "ORDER DEAL",
                    key=deal["id"],
                    width="stretch"
                ):

                    st.session_state.cart.append({
                        "id": deal["id"],
                        "name": deal["name"],
                        "price": deal["price"],
                        "image": PRODUCTS[0]["image"],
                        "quantity": 1
                    })

                    st.toast(
                        f"{deal['name']} added!"
                    )

# ============================================================
# CART
# ============================================================
elif page == "Cart":

    st.markdown(
        '<div class="section-title">Your Cart</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.cart:

        st.info(
            "Your cart is empty."
        )

    else:

        # Display cart
        for item in st.session_state.cart:

            st.markdown(
                '<div class="cart-item">',
                unsafe_allow_html=True
            )

            col1, col2, col3 = st.columns(
                [1, 3, 1]
            )

            with col1:

                st.image(
                    item["image"],
                    width=90
                )

            with col2:

                st.markdown(
                    f"### {item['name']}"
                )

                st.write(
                    rupiah(item["price"])
                )

                st.write(
                    f"Quantity: {item['quantity']}"
                )

            with col3:

                if st.button(
                    "REMOVE",
                    key=f"remove_{item['id']}"
                ):

                    remove_from_cart(item["id"])
                    st.rerun()

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

        # Total
        total = total_price()

        st.markdown(
            f"""
            <div class="cart-total">

                <div>ORDER TOTAL</div>

                <div class="total-price">
                    {rupiah(total)}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### Checkout")

        name = st.text_input(
            "Name",
            placeholder="Your name"
        )

        phone = st.text_input(
            "Phone",
            placeholder="08xxxxxxxxxx"
        )

        order_type = st.selectbox(
            "Order Type",
            [
                "Delivery",
                "Pickup"
            ]
        )

        address = ""

        if order_type == "Delivery":

            address = st.text_area(
                "Delivery Address",
                placeholder="Your full address"
            )

        payment = st.selectbox(
            "Payment",
            [
                "Cash",
                "QRIS",
                "GoPay",
                "OVO",
                "DANA",
                "Bank Transfer"
            ]
        )

        if st.button(
            "🔥 PLACE ORDER",
            width="stretch"
        ):

            valid = True

            if not name.strip():

                st.error(
                    "Please enter your name."
                )

                valid = False

            if not phone.strip():

                st.error(
                    "Please enter your phone number."
                )

                valid = False

            if order_type == "Delivery" and not address.strip():

                st.error(
                    "Please enter your address."
                )

                valid = False

            if valid:

                order_id = (
                    "N1C-"
                    + datetime.now().strftime(
                        "%Y%m%d%H%M%S"
                    )
                )

                st.session_state.orders.append({
                    "order_id": order_id,
                    "name": name,
                    "phone": phone,
                    "total": total,
                    "order_type": order_type,
                    "payment": payment
                })

                st.session_state.cart = []

                st.success(
                    f"Order {order_id} successfully placed!"
                )

                st.balloons()

# ============================================================
# ABOUT
# ============================================================
elif page == "About":

    st.markdown(
        '<div class="section-title">'
        'About Number 1 Chicken'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        """
        Number 1 Chicken is a modern fast-food franchise
        focused on crispy chicken, burgers, family meals,
        sides and refreshing drinks.

        Our goal is simple:

        **Great food, great value, great experience.**
        """
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Our Mission")

        st.write(
            "Serve delicious fast food while keeping "
            "quality, speed and value at the center."
        )

    with col2:

        st.markdown("### Franchise")

        st.write(
            "A scalable restaurant concept designed "
            "for locations across Indonesia."
        )

# ============================================================
# FOOTER
# ============================================================
st.markdown(textwrap.dedent("""
    <div class="footer">
        <div class="footer-title">
            NUMBER 1 CHICKEN
        </div>
        <p>
            CRISPY. JUICY. UNFORGETTABLE.
        </p>
        <p>
            © 2026 Number 1 Chicken
        </p>
    </div>
    """), unsafe_allow_html=True)
