# Simple Blockchain Implementation

This Python code illustrates how a blockchain works in an easily readable and understandable format. Actual live blockchains run on the same exact principles illustrated here.

While this Python code would not make for a secure *production* blockchain, it makes it easy to experiment with blockchain technology and understanding how and *why* it works the way it does.

## blockchain.py

The `blockchain.py` file is a **library** that implements a simple blockchain as a pair of classes: `Block` and `Blockchain`.

The `Block` class represents an individual block on the blockchain. Recall that a blockchain is simply a "chain" of data blobs, where each data entry is cryptographically linked to the previous entry. Verifying the chain integrity involves working forward from the block immediately following the initial "genesis" block and verifying blocks forward until the current block is reached. This process can be relatively quickly repeated and done by anyone with a copy of the entire chain at any time. **The cryptographic security of the hashes gives blockchain its immutability and security** - a blockchain does not, on its own, *prevent* tampering of data, but it *does* prevent *invisible tampering* with data - that is, a pure blockchain can *identify* that data has been tampered with, but it cannot, on its own, *repair* that data.

> In practice, production blockchains use consensus as a recovery mechanism. If an error in the block is found, *many* nodes in the network will validate the chain; once *enough* nodes have validated their own version of the chain, that specific chain becomes the new "authoritative" chain, and the chain that failed validation is, by definition, forgotten and discarded.
>
> One of the largest blockchain networks, Bitcoin, has tens of thousands of nodes, each of which possess a complete copy of the authoritative blockchain. For a successful attack to happen, *enough nodes would need to simultaneously coordinate an attack* involving modifying the data on *all* of those nodes nearly instantaneously to the new desired state. This is made even more difficult because this attack would still *not* remove the requirement to "mine" the block being modified *and all future blocks since that block* - this is an operation that is, at this time, computationally infeasible.

The `Blockchain` class implements a full blockchain using `Block` objects. You can insert any arbitrary data you want into a block and the blockchain will mine the block, producing a valid signature, causing the block to be "valid" within the chain.

## example.py

`example.py` is a runnable script that shows you an example of the blockchain in action. Some data is added and then tampering is attempted.

The difficulty level of the blockchain is set low to make sure that the mining process is achievable in a very short time on a modern PC. However, the difficulty can scale up as far as it needs to - this is why it requires massive powerful machines to mine Bitcoin. (In Bitcoin, there are extra algorithms in place that regulate the network difficulty *based on the speed of successful block mining* - this ensures that the rate of valid block generation remains *roughly* constant over time. As more and more people with extremely powerful hashing systems came online, the difficulty of the network adapted to keep the generation rate constant - this is why it's all but impossible to successfully mine Bitcoin using only a CPU or a small GPU today.)
