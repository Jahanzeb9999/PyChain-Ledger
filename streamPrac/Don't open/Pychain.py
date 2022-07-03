{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fa0ed913-0579-4a75-8e4c-30ca1e5de054",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting hashlib\n",
      "  Using cached hashlib-20081119.zip (42 kB)\n",
      "  Preparing metadata (setup.py): started\n",
      "  Preparing metadata (setup.py): finished with status 'error'\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  error: subprocess-exited-with-error\n",
      "  \n",
      "  python setup.py egg_info did not run successfully.\n",
      "  exit code: 1\n",
      "  \n",
      "  [7 lines of output]\n",
      "  Traceback (most recent call last):\n",
      "    File \"<string>\", line 2, in <module>\n",
      "    File \"<pip-setuptools-caller>\", line 34, in <module>\n",
      "    File \"C:\\Users\\jahan\\AppData\\Local\\Temp\\pip-install-s3ybp1ba\\hashlib_ff5c915b699240998b33efc421f672c7\\setup.py\", line 68\n",
      "      print \"unknown OS, please update setup.py\"\n",
      "            ^\n",
      "  SyntaxError: Missing parentheses in call to 'print'. Did you mean print(\"unknown OS, please update setup.py\")?\n",
      "  [end of output]\n",
      "  \n",
      "  note: This error originates from a subprocess, and is likely not a problem with pip.\n",
      "error: metadata-generation-failed\n",
      "\n",
      "Encountered error while generating package metadata.\n",
      "\n",
      "See above for output.\n",
      "\n",
      "note: This is an issue with the package mentioned above, not pip.\n",
      "hint: See above for details.\n"
     ]
    }
   ],
   "source": [
    "pip install hashlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "51d85c75-63ac-4f25-8e8a-c0aa93cc0824",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-06-25 13:59:45.429 INFO    numexpr.utils: NumExpr defaulting to 6 threads.\n"
     ]
    }
   ],
   "source": [
    "# Imports\n",
    "import hashlib\n",
    "import streamlit as st\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "eaf7b5e0-4906-45f6-8565-12d8b02b7a73",
   "metadata": {},
   "outputs": [],
   "source": [
    "from dataclasses import dataclass\n",
    "from typing import Any, List\n",
    "import datetime as datetime\n",
    "import hashlib\n",
    "\n",
    "@dataclass\n",
    "class Block:\n",
    "    data: Any\n",
    "    creator_id: int\n",
    "    timestamp: str = datetime.datetime.utcnow().strftime(\"%H:%M:%S\")\n",
    "    prev_hash: str = \"0\"\n",
    "    nonce: int = 0\n",
    "    \n",
    "    \n",
    "    def hash_block(self):\n",
    "        sha = hashlib.sha256()\n",
    "\n",
    "        data = str(self.data).encode()\n",
    "        sha.update(data)\n",
    "\n",
    "        creator_id = str(self.creator_id).encode()\n",
    "        sha.update(data)\n",
    "\n",
    "        prev_hash = str(self.prev_hash).encode()\n",
    "        sha.update(prev_hash)\n",
    "\n",
    "        timestamp = str(self.timestamp).encode()\n",
    "        sha.update(timestamp)\n",
    "\n",
    "        nonce = str(self.nonce).encode()\n",
    "        sha.update(nonce)\n",
    "\n",
    "        return sha.hexdigest()\n",
    "\n",
    "@dataclass\n",
    "class Pychain:\n",
    "    chain: List[Block]\n",
    "    difficulty: int = 4\n",
    "    \n",
    "    def proof_of_work(self, block):\n",
    "        calculated_hash = block.hash_block()\n",
    "        \n",
    "        num_of_zeros = \"0\" * self.difficulty\n",
    "        \n",
    "        while not calculated_hash.startswith(num_of_zeros):\n",
    "            block.nonce += 1\n",
    "            calculated_hash = block.hash_block()\n",
    "            \n",
    "        return block\n",
    "    def add_block(self, candidate_block):\n",
    "        block = self.proof_of_work(candidate_block)\n",
    "        self.chain += [block]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "34d9bde0-b3f6-4c97-9cdb-85317961ad02",
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
   "version": "3.8.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
