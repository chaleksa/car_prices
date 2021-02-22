import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64


def get_image():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()

    return graph


def get_simple_plot(data, *args):

    sns.set()
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(8, 5))

    fig.patch.set_facecolor((0.73, 0.72, 0.72))
    fig.patch.set_alpha(0.85)

    # text_color = 'white'
    # plt.rcParams['text.color'] = text_color
    # plt.rcParams['axes.labelcolor'] = text_color
    # plt.rcParams['xtick.color'] = text_color
    # plt.rcParams['ytick.color'] = text_color

    print(plt.rcParams)

    plt.hist(data, color=(0.023, 0.68, 0.73))
    plt.title(
        f'Prices Distribution \n {" ".join([i for i in args if i])}')
    plt.xlabel('price ($)')
    plt.ylabel('number of offers')
    plt.grid(True)
    plt.tight_layout()
    graph = get_image()
    return graph


def params_list(a, b):
    params_list = list(
        filter(None, [a, b]))
    params_list.sort()

    return params_list
