{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab01dc95-29cc-42c1-b94d-747936d3bf2e",
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
