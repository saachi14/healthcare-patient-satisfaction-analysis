import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a pandas DataFrame
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Satisfaction": [-0.01, 1.1, 7.92, 6.62]
}
df = pd.DataFrame(data)

# Step 2: Calculate the exact average
average_score = df["Satisfaction"].mean()
print(f"Calculated Average: {average_score:.2f}")

# Step 3: Plot the quarterly scores as a line chart
plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["Satisfaction"], marker='o', linestyle='-', label="Quarterly Scores")

# Step 4: Add a horizontal line for the industry benchmark target (4.5)
plt.axhline(y=4.5, color="red", linestyle="--", label="Industry Benchmark (4.5)")

# Step 5: Add a horizontal line for the current average
plt.axhline(y=average_score, color="green", linestyle=":", label=f"Average ({average_score:.2f})")

# Step 6: Label the lines clearly (done via legend)
plt.legend()

# Step 7: Add title and labels
plt.title("Patient Satisfaction Trend (2024)")
plt.xlabel("Quarter")
plt.ylabel("Satisfaction Score")

# Step 8: Save the plot
plt.tight_layout()
plt.savefig("patient_satisfaction_trend.png", dpi=300)
plt.show()
