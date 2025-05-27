import hashlib
import json
import time
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple

class Block:
    """Represents a block of data on the blockchain."""

    def __init__(self, index: int, timestamp: float, data: Dict[str, Any], previous_hash: str):
        """
        Initialize a new block in the blockchain
        
        Args:
            index: Position of the block in the chain
            timestamp: Time when the block was created
            data: The data to be stored in the block
            previous_hash: Hash of the previous block
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """Calculate the hash of this block."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        
        return hashlib.sha256(block_string).hexdigest()
    
    def get_leading_hash_zeroes(self, hash) -> int:
        # Assume that the hash is a hex digest without leading 0x
        # Convert the hash to binary
        binary_hash = bin(int(hash, 16))[2:].zfill(256)
        # Count leading zeros
        leading_zeros = len(binary_hash) - len(binary_hash.lstrip('0'))
        return leading_zeros

    def mine_block(self, difficulty: int) -> None:
        """
        Mine a block (find a hash with the specified number of leading binary zeros)
        
        Args:
            difficulty: Number of leading binary zeros required in the hash
        """
        
        while self.get_leading_hash_zeroes(self.calculate_hash()) != difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        
        print(f"Block mined: {self.hash}")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the block to a dictionary."""
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "hash": self.hash
        }
    
    def __str__(self) -> str:
        """String representation of the block."""
        formatted_time = datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')
        return (f"Block #{self.index}\n"
                f"Timestamp: {formatted_time}\n"
                f"Data: {json.dumps(self.data, indent=2)}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Hash: {self.hash}\n"
                f"Nonce: {self.nonce}\n")

class Blockchain:
    def __init__(self, difficulty: int = 2):
        """
        Initialize a new blockchain
        
        Args:
            difficulty: The mining difficulty (number of leading zeros in hash)
        """
        self.chain: List[Block] = []
        self.difficulty = difficulty
        
        # Create the genesis block
        self.create_genesis_block()
    
    def create_genesis_block(self) -> None:
        """Create the first block in the blockchain."""
        genesis_block = Block(0, time.time(), {"message": "Genesis Block"}, "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
    
    def get_latest_block(self) -> Block:
        """Get the most recent block in the blockchain."""
        return self.chain[-1]
    
    def add_block(self, data: Dict[str, Any]) -> Block:
        """
        Add a new block to the blockchain with the given data
        
        Args:
            data: The data to add to the blockchain
            
        Returns:
            The newly created and added block
        """
        previous_block = self.get_latest_block()
        new_index = previous_block.index + 1
        new_block = Block(new_index, time.time(), data, previous_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        return new_block
    
    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid by verifying each block's hash and links
        
        Returns:
            True if the blockchain is valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash at block {i}: {current_block.hash} vs {current_block.calculate_hash()}")
                return False
            
            # Check if the current block points to the correct previous hash
            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid previous hash at block {i}: {current_block.previous_hash} vs {previous_block.hash}")
                return False
        
        return True
    
    def find_blocks_by_criteria(self, key: str, value: Any) -> List[Block]:
        """
        Search for blocks containing specific data based on key-value pairs
        
        Args:
            key: The key to search for in the data dictionary
            value: The value to match
            
        Returns:
            List of blocks matching the criteria
        """
        matching_blocks = []
        
        for block in self.chain:
            if key in block.data and block.data[key] == value:
                matching_blocks.append(block)
        
        return matching_blocks
    
    def get_block_by_index(self, index: int) -> Optional[Block]:
        """
        Get a block by its index
        
        Args:
            index: The index of the block to retrieve
            
        Returns:
            The block if found, None otherwise
        """
        if 0 <= index < len(self.chain):
            return self.chain[index]
        return None
    
    def attempt_tamper(self, block_index: int, new_data: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Attempt to tamper with a block to demonstrate blockchain security
        
        Args:
            block_index: The index of the block to tamper with
            new_data: The new data to put in the block
            
        Returns:
            A tuple of (success, message)
        """
        if block_index < 0 or block_index >= len(self.chain):
            return False, "Invalid block index"
        
        # Try to change the data
        original_data = self.chain[block_index].data.copy()
        self.chain[block_index].data = new_data
        
        # Check if the chain is still valid
        if self.is_chain_valid():
            return True, "Tamper successful (this should not happen in a proper blockchain)"
        else:
            # Restore the original data
            self.chain[block_index].data = original_data
            return False, "Tamper detected, blockchain protected the data"
    
    def __str__(self) -> str:
        """String representation of the entire blockchain."""
        chain_repr = "\n".join(str(block) for block in self.chain)
        return f"Blockchain (length: {len(self.chain)}):\n{chain_repr}"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the blockchain to a dictionary."""
        return {
            "chain": [block.to_dict() for block in self.chain],
            "difficulty": self.difficulty,
            "length": len(self.chain)
        }
    
    def to_json(self, indent: int = 2) -> str:
        """Convert the blockchain to a JSON string."""
        return json.dumps(self.to_dict(), indent=indent)
    
    def save_to_file(self, filename: str) -> None:
        """Save the blockchain to a file."""
        with open(filename, 'w') as file:
            file.write(self.to_json())
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'Blockchain':
        """Load a blockchain from a file."""
        with open(filename, 'r') as file:
            data = json.load(file)
        
        blockchain = cls(difficulty=data['difficulty'])
        blockchain.chain = []  # Clear the genesis block
        
        for block_data in data['chain']:
            block = Block(
                index=block_data['index'],
                timestamp=block_data['timestamp'],
                data=block_data['data'],
                previous_hash=block_data['previous_hash']
            )
            block.nonce = block_data['nonce']
            block.hash = block_data['hash']
            blockchain.chain.append(block)
        
        return blockchain
