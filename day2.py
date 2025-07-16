{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "65d25bf1-12d4-429d-a94a-d6eecb31edc3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "# Type Conversion\n",
    "# Explicit\n",
    "x = 10\n",
    "y = float(x)\n",
    "print(type(y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "421675ac-9db8-4e88-a83f-c111c162037d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "# Implicit\n",
    "x = 10\n",
    "y = 10.5\n",
    "print(type(x+y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "62b54720-0b04-4e3a-acf6-0c731a028cb5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter The Name Of Product: Milk\n",
      "Enter The Quantity of product: 1\n",
      "Enter The Price: 60\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Product is: Milk Total Price:  60.0\n"
     ]
    }
   ],
   "source": [
    "# Que\n",
    "productName = input(\"Enter The Name Of Product:\")\n",
    "quantity = int(input(\"Enter The Quantity of product:\"))\n",
    "price = float(input(\"Enter The Price:\"))\n",
    "Total = quantity*price\n",
    "print(\"Product is:\",productName,\"Total Price: \",Total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a55cf149-fde9-4e75-bb1e-a2b68ec399e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exit\n"
     ]
    }
   ],
   "source": [
    "# Data Control Flow Structure\n",
    "# if else elif\n",
    "a = 10\n",
    "if a > 15:\n",
    "    print(\"Hello\")\n",
    "else:\n",
    "    print(\"Exit\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f0b20c21-b3a4-4699-b4a3-5d38bd132b0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a Number: -9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number is Negative.\n"
     ]
    }
   ],
   "source": [
    "# que assignment 1\n",
    "num = int(input(\"Enter a Number:\"))\n",
    "if num > 0 :\n",
    "    print(\"Number is positive.\")\n",
    "elif num < 0:\n",
    "    print(\"Number is Negative.\")\n",
    "else :\n",
    "    print(\"Number is zero.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "10f24d7b-27b0-4eb8-824d-45159b841ae8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your age -89\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Invalid Age\n"
     ]
    }
   ],
   "source": [
    "# que assignment 2\n",
    "age=int(input(\"enter your age\"))\n",
    "if age >=0 :\n",
    "    if age>=18:\n",
    "        print(\"eligible to vote\")\n",
    "    else:\n",
    "        print(\"not eligible\")\n",
    "else :\n",
    "    print(\"Invalid Age\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "36a7bae0-252a-4f8b-aed2-4567bfdcd1e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a Number: 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number is Odd.\n"
     ]
    }
   ],
   "source": [
    "# que assignment 3\n",
    "num = int(input(\"Enter a Number:\"))\n",
    "if num%2 == 0 :\n",
    "    print(\"Number is Even.\")\n",
    "else :\n",
    "    print(\"Number is Odd.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "ae98d35c-80d8-4625-917b-e494a8005a49",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter String: sneha\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Length of String is greater less 5\n"
     ]
    }
   ],
   "source": [
    "# que assignment 4\n",
    "str = input(\"Enter String:\")\n",
    "if len(str) > 5 :\n",
    "    print(\"Length of String is greater than 5\")\n",
    "else :\n",
    "    print(\"Length of String is greater less 5\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "d7a49c02-985e-4d76-95e5-a0956cf5b1cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your marks 32\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fail\n"
     ]
    }
   ],
   "source": [
    "# que assignment 5\n",
    "marks = int(input(\"enter your marks\"))\n",
    "if marks >= 40:\n",
    "    print(\"pass\")\n",
    "else:\n",
    "    print(\"fail\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "afc4ecc6-2dca-495f-bf8e-819c38240798",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
