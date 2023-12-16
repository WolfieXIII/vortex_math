"""
Vortex Plot
By Jack Seymour
Created on 12/14/23
"""
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import random


def filter_colors(color_list, low_threshold=0.3, high_threshold=0.7):
    """
    Filters out colors that are too close to white or black.

    Args:
    color_list (list): List of color names.
    low_threshold (float): Lower bound for luminance.
    high_threshold (float): Upper bound for luminance.

    Returns:
    list: Filtered list of color names.
    """
    filtered_colors = []

    for color_name in color_list:
        # Convert color name to RGB
        rgb = mcolors.to_rgb(color_name)

        # Calculate luminance (using a common formula for perceived brightness)
        luminance = 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]

        # Check if the color is within the desired luminance range
        if low_threshold <= luminance <= high_threshold:
            filtered_colors.append(color_name)

    return filtered_colors


def digital_root(n, mod=9):
    """
    Compute the digital root of N

    Args:
        n (int) : number
        mod (int) : modulus used to compute the root

    Returns:
        int: digital root of N
    """
    return (n - 1) % mod + 1 if n != 0 else 0


def plot_modulus_circle(start=2, multiplier=2, modulus=9, iterations=18,
                        direction=True, point_order_clockwise=True, offset_angle=90,
                        background_color='black', text_color='white', recursive=True):
    """
    Plot a circle with points equidistant on the circumference.
    Connect the points according to the progression of numbers
    following the rule: new_number = (current_number * multiplier) % modulus.

    Args:
    start (int, optional): Starting point of the plot
    multiplier (int, optional): The multiplier used to calculate the next number.
    modulus (int, optional): The modulus to wrap the circle.
    iterations (int, optional): Number of iterations to plot the progression.
    direction (bool, optional): True for 'forward', False for 'backward' progression direction.
    point_order_clockwise (bool, optional): Whether to plot points in clockwise order.
    offset_angle (float, optional): The angle in degrees to offset the point positions.
    recursive (bool, optional): Whether to recursively plot the path

    Returns:
    None
    """
    # Calculate scaling factors based on modulus
    scale_factor = max(1, modulus / 20)
    text_scale = max(12, 30 - modulus // 3)

    offset = offset_angle - 360 / modulus
    offset_radians = np.radians(offset)

    if point_order_clockwise:
        angles = np.linspace(0, -2 * np.pi, modulus, endpoint=False) + offset_radians
    else:
        angles = np.linspace(0, 2 * np.pi, modulus, endpoint=False) - offset_radians

    x = np.cos(angles) * scale_factor
    y = np.sin(angles) * scale_factor

    # Adjust the figure size for better visibility
    fig, ax = plt.subplots(figsize=(10, 10))  # You can adjust the size here

    # Set the background colors
    ax.set_facecolor(background_color)  # Set the plot area background color
    fig.set_facecolor(background_color)  # Set the entire figure background color

    circle = plt.Circle((0, 0), scale_factor, color='gray', fill=False)
    ax.add_artist(circle)

    for i in range(modulus):
        xi = x[i]
        yi = y[i]
        plt.plot(xi, yi, 'o', color='orange')
        plt.text(xi * 1.1, yi * 1.1, str(i + 1), fontsize=text_scale, ha='center', va='center', color=text_color)

    visited = set()
    colors = [
        'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure',
        'beige', 'bisque', 'black', 'blanchedalmond', 'blue',
        'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse',
        'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson',
        'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray',
        'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen',
        'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen',
        'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet',
        'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue',
        'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro',
        'ghostwhite', 'gold', 'goldenrod', 'gray', 'green',
        'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred',
        'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush',
        'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan',
        'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink',
        'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey',
        'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen',
        'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid',
        'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise',
        'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin',
        'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab',
        'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen',
        'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru',
        'pink', 'plum', 'powderblue', 'purple', 'red',
        'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown',
        'seagreen', 'seashell', 'sienna', 'silver', 'skyblue',
        'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen',
        'steelblue', 'tan', 'teal', 'thistle', 'tomato',
        'turquoise', 'violet', 'wheat', 'white', 'whitesmoke',
        'yellow', 'yellowgreen'
    ]
    color_index = 0
    colors.remove(background_color)
    colors.remove(text_color)
    colors = filter_colors(colors)

    def plot_path(_start, color):
        current_number = _start
        for _ in range(iterations):
            if direction:
                next_number = digital_root(current_number * multiplier, modulus)
            else:
                inverse_multiplier = pow(multiplier, -1, modulus)
                next_number = digital_root(current_number * inverse_multiplier, modulus)

            start_angle = angles[current_number - 1]
            end_angle = angles[next_number - 1]
            ax.annotate("", xy=(np.cos(end_angle) * scale_factor, np.sin(end_angle) * scale_factor),
                        xycoords='data',
                        xytext=(np.cos(start_angle) * scale_factor, np.sin(start_angle) * scale_factor),
                        textcoords='data',
                        arrowprops=dict(arrowstyle="->", color=color, lw=1.00))
            visited.add(current_number)
            if next_number == start:
                break
            current_number = next_number

    # Plot the initial path
    _c = random.choice(colors)
    plot_path(start, _c)  # colors[color_index % len(colors)])
    color_index += 1

    if recursive:
        # Plot paths for unvisited points
        for point in range(1, modulus + 1):
            if point not in visited and point != modulus:  # Skipping the final point
                _c = random.choice(colors)
                plot_path(point, _c)  # colors[color_index % len(colors)])
                color_index += 1

    # Dynamically adjust plot limits based on scale factor
    plot_limit = scale_factor * 1.5
    ax.set_aspect('equal')
    ax.set_xlim([-plot_limit, plot_limit])
    ax.set_ylim([-plot_limit, plot_limit])
    ax.axis('off')
    plt.show()


if __name__ == '__main__':
    _start = 1
    _multiplier = 7
    _modulus = 100
    _iterations = _modulus

    plot_modulus_circle(start=_start, multiplier=_multiplier, modulus=_modulus, iterations=_iterations,
                        direction=True, point_order_clockwise=True, offset_angle=90, recursive=True)
