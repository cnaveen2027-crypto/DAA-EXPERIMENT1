from flask import Flask, request, render_template_string

app = Flask(__name__)

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:

        if low == high:
            if arr[low] == target:
                return low
            return -1

        if arr[high] == arr[low]:
            break

        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Interpolation Search</title>
</head>
<body>
    <h2>Interpolation Search</h2>

    <form method="POST">
        <label>Array Elements (space separated):</label><br>
        <input type="text" name="array" required><br><br>

        <label>Target Element:</label><br>
        <input type="number" name="target" required><br><br>

        <button type="submit">Search</button>
    </form>

    {% if result is not none %}
        <h3>{{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        arr = list(map(int, request.form["array"].split()))
        arr.sort()

        target = int(request.form["target"])

        idx = interpolation_search(arr, target)

        if idx != -1:
            result = f"Element found at index {idx}"
        else:
            result = "Element not found"

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
