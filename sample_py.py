{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPahKlzQU4UrLjUDWg93xuR",
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
        "<a href=\"https://colab.research.google.com/github/divyakola/my-site/blob/master/sample_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T05GHr1RIxoL",
        "outputId": "b8fc1fd2-755b-4508-cf01-7c0d8fc21d42"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello world\n"
          ]
        }
      ],
      "source": [
        "print(\"hello world\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "write a python program to perform arithmetic calculations?"
      ],
      "metadata": {
        "id": "CxWz_BX8I7nl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x=10\n",
        "y=20\n",
        "print(x+y)\n",
        "print(x-y)\n",
        "print(x*y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jfi1cnloJAzn",
        "outputId": "c548534d-73ca-4466-afb6-9302ec3af2f8"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "30\n",
            "-10\n",
            "200\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# prompt: write a python program to find the factorial of the given number?\n",
        "\n",
        "def factorial(n):\n",
        "  if n == 0:\n",
        "    return 1\n",
        "  else:\n",
        "    return n * factorial(n-1)\n",
        "\n",
        "# Get the input from the user\n",
        "n = int(input(\"Enter a number: \"))\n",
        "\n",
        "# Print the factorial of the number\n",
        "print(\"The factorial of\", n, \"is\", factorial(n))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3uUF4FOmJG1A",
        "outputId": "d5c22680-74c2-4132-de63-ccd25aa88658"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 5\n",
            "The factorial of 5 is 120\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# prompt: write a python program to find the area of the circle\n",
        "\n",
        "import math\n",
        "\n",
        "def area_of_circle(radius):\n",
        "  \"\"\"\n",
        "  This function calculates the area of a circle given its radius.\n",
        "\n",
        "  Args:\n",
        "      radius: The radius of the circle in meters.\n",
        "\n",
        "  Returns:\n",
        "      The area of the circle in square meters.\n",
        "  \"\"\"\n",
        "  return math.pi * radius ** 2\n",
        "\n",
        "# Get the radius of the circle from the user\n",
        "radius = float(input(\"Enter the radius of the circle in meters: \"))\n",
        "\n",
        "# Calculate and print the area of the circle\n",
        "area = area_of_circle(radius)\n",
        "print(\"The area of the circle is\", area, \"square meters.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3y-edBOmJYmG",
        "outputId": "bb2c8f0e-36c0-49a3-ef94-b30a63fdbc0b"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the radius of the circle in meters: 5\n",
            "The area of the circle is 78.53981633974483 square meters.\n"
          ]
        }
      ]
    }
  ]
}