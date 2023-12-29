{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15529b80-8570-4b36-9af6-99cc00a06698",
   "metadata": {},
   "outputs": [],
   "source": [
    "from openai import OpenAI\n",
    "client = OpenAI()\n",
    "\n",
    "completion = client.chat.completions.create(\n",
    "  model=\"gpt-3.5-turbo\",\n",
    "  messages=[\n",
    "    {\"role\": \"system\", \"content\": \"You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.\"},\n",
    "    {\"role\": \"user\", \"content\": \"Compose a poem that explains the concept of recursion in programming.\"}\n",
    "  ]\n",
    ")\n",
    "\n",
    "print(completion.choices[0].message)"
   ]
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
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
