{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "cc38f03e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter no. of test cases6\n",
      "Enter no,=1\n",
      "1\n",
      "Enter no,=2\n",
      "0\n",
      "Enter no,=3\n",
      "1\n",
      "Enter no,=4\n",
      "1\n",
      "Enter no,=8\n",
      "0\n",
      "Enter no,=48\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "t=int(input(\"Enter no. of test cases\"))\n",
    "while t:\n",
    "    n=int(input(\"Enter no,=\"))\n",
    "    c=0\n",
    "    while n%2==0:\n",
    "        n=n//2\n",
    "        c+=1 \n",
    "    if c%2==0:\n",
    "        print(\"1\")\n",
    "    else:\n",
    "        print(\"0\")\n",
    "    t-=1\n",
    "\n",
    "            \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f80e43dd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e986099c",
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
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
