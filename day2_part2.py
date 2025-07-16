{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "cd112e16-daa7-4c00-bd55-130623c86a7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Month Name: February \n"
     ]
    }
   ],
   "source": [
    "# Elif \n",
    "# Que 1\n",
    "month = input(\"Enter Month Name:\")\n",
    "\n",
    "if month == \"January\" or month == \"November\" or month == \"December\" :\n",
    "    print(\"Winter Season\")\n",
    "elif  month == \"February\" or month == \"March\":\n",
    "    print(\"Spring Season\")\n",
    "elif month == \"April\" or month == \"May\"or month==\"June\"  :\n",
    "    print(\"Summar Season\")\n",
    "elif month ==\"October\"or month==\"September\":\n",
    "    print(\"Autumn Season\")\n",
    "elif month == \"July\" or month == \"August\" :\n",
    "    print(\"Rain Season\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "f9589ab7-6f07-4657-9222-c52e840f31bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Name Of Your Vehicle: Scooty\n",
      "Enter Year: 2025\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your Scooty expire after 2040\n"
     ]
    }
   ],
   "source": [
    "# que \n",
    "vehicle = input(\"Enter Name Of Your Vehicle options(Car,Bike,Scooty):\")\n",
    "year = int(input(\"Enter Year:\"))\n",
    "expireCar = 20\n",
    "expirBike = 10\n",
    "expireScooty = 15\n",
    "if vehicle == \"Car\" :\n",
    "    print(\"Your car expire after\",year+expireCar)\n",
    "elif vehicle == \"Bike\":\n",
    "    print(\"Your Bike expire after\",year+expireBike)\n",
    "elif vehicle == \"Scooty\":\n",
    "    print(\"Your Scooty expire after\",year+expireScooty)\n",
    "else :\n",
    "    print(\"Invalid\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f1868e0b-178f-4a70-b113-2e4f6b292bac",
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
