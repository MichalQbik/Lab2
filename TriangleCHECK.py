{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMTDJws9YS5Bvxglje4+d2E",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MichalQbik/Lab2/blob/main/TriangleCHECK.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 34,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XGoMF5Y2x0ow",
        "outputId": "db5319dd-77a8-4051-d0ac-a20a7c251160"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ],
      "source": [
        "def check (a,b,c):\n",
        "  if a + b >= c and a + c >= b and b + c >= a:\n",
        "    print(\"True\")\n",
        "  else:\n",
        "    print(\"False\")\n",
        "\n",
        "check(3,4,5)\n",
        ""
      ]
    }
  ]
}