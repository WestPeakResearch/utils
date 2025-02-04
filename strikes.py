import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from datetime import datetime

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = [".SF NS Text", "Helvetica", "Arial"]

with open("roster.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def plot_block_chart(ax, category_name, members):
    names = list(members.keys())
    values = list(members.values())

    y_positions = list(range(len(names)))[::-1]

    ax.set_facecolor("#0a233d")
    ax.set_title(category_name, fontsize=14, pad=0, fontweight="bold", color="white")

    for y_pos, (name, value) in zip(y_positions, members.items()):
        if value == 0:
            ax.barh(y_pos, 1, color="grey", height=0.6)
            ax.barh(y_pos, 1, left=1, color="grey", height=0.6)
            ax.barh(y_pos, 1, left=2, color="grey", height=0.6)
            ax.text(-0.2, y_pos, name, fontsize=10, color="grey", verticalalignment="center", ha="right")
        elif value == 1:
            ax.barh(y_pos, 1, color="#fab387", height=0.6)
            ax.barh(y_pos, 1, left=1, color="grey", height=0.6)
            ax.barh(y_pos, 1, left=2, color="grey", height=0.6)
            ax.text(-0.2, y_pos, name, fontsize=10, color="#fab387", verticalalignment="center", ha="right")
        elif value == 2:
            ax.barh(y_pos, 1, color="#fab387", height=0.6)
            ax.barh(y_pos, 1, left=1, color="#ff6173", height=0.6)
            ax.barh(y_pos, 1, left=2, color="grey", height=0.6)
            ax.text(-0.2, y_pos, name, fontsize=10, color="#ff6173", verticalalignment="center", ha="right")

    # Formatting axes
    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.set_xlim(-1, 3.5)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

# Create figure with two vertically stacked subplots
fig, axes = plt.subplots(2, 1, figsize=(10, 12), sharex=True)

fig.set_facecolor("#0a233d")

# Plot Juniors and Seniors
plot_block_chart(axes[0], "Junior Analysts", data["juniors"])
plot_block_chart(axes[1], "Senior Analysts", data["seniors"])

# Add main title
suptitle = fig.suptitle("WestPeak Research Association Analysts Strikes", color="white", fontsize=16, fontweight="bold", x=0.525)
suptitle.set(family="Arial")

# Add logo image next to the suptitle
#img = mpimg.imread('logo.jpg')  # Replace with the path to your image
#fig.figimage(img, xo=500, yo=330, alpha=0.8, zorder=10, resize=True)  # Adjust position of the logo# Adjust image position and transparency

# Add generated date at the bottom
generated_date = datetime.now().strftime("Generated on %Y %B %-d")
fig.text(0.5, 0.02, generated_date, ha="center", fontsize=10, color="white")

# Adjust layout and save the image
plt.tight_layout(rect=[0, 0.025, 1, 0.98])  # Leave space for date at the bottom
plt.savefig("strikes.png", dpi=300)
