import pandas as pd

#Create a dummy feedback dataset
data = {
    "customer_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "feedback": [
        "Great service!",
        "Very satisfied with the product.",
        "Not happy with the delivery time.",
        "Excellent customer support.",
        "Product quality could be better.",
        "Will definitely recommend to others.",
        "Had a bad experience with the return process.",
        "Loved the packaging!",
        "Customer service was very helpful.",
        "Overall, a good experience."
    ]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("customer_feedback.csv", index=False)

# COnfirmation message
print("Dummy customer feedback dataset created and saved as 'customer_feedback.csv'")