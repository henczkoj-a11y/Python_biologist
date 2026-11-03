
import matplotlib.pyplot as plt


def print_report(counts):
    total = sum(counts.values())

    print("Mutation Simulation Report")
    print("--------------------------")

    for category, count in counts.items():
        percentage = (count / total * 100) if total > 0 else 0
        print(f"{category}: {count} ({percentage:.2f}%)")


def plot_results(counts):
    plt.bar(counts.keys(), counts.values())
    plt.title("Mutation Simulation Results")
    plt.xlabel("Mutation effect")
    plt.ylabel("Number of mutations")
    plt.show()


if __name__ == "__main__":
    # Example data for testing
    counts = {
        "silent": 120,
        "missense": 650,
        "nonsense": 30,
        "frameshift": 200
    }

    print_report(counts)
    plot_results(counts)

