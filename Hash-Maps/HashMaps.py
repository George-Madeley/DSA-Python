class HashMap:
    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(size)]

    def hash(self, key, collisionCount):
        keyBytes = key.encode
        hashCode = sum(keyBytes)
        return hashCode + collisionCount

    def Compressor(self, hashCode):
        return hashCode % self.size

    def assign(self, key, value):
        hashCode = self.hash(key)
        index = self.Compressor(hashCode)
        currentValue = self.array[index]
        if currentValue is None:
            self.array[index] = [key, value]
        elif currentValue[0] == key:
            self.array[index] = [key, value]
        else:
            numberOfCollisions = 1
            while currentValue[0] != key:
                hashCode = self.hash(key, numberOfCollisions)
                index = self.Compressor(hashCode)
                currentValue = self.array[index]
                if currentValue is None:
                    self.array[index] = [key, value]
                    return
                if currentValue[0] == key:
                    self.array[index] = [key, value]
                    return
                number_collisions += 1
                return

    def retrieve(self, key):
        hashCode = self.hash(key)
        index = self.Compressor(hashCode)
        possibleValue = self.array[index]
        if possibleValue is None:
            return None
        elif possibleValue[0] == key:
            return possibleValue[1]
        else:
            numberOfCollisions = 1
            while possibleValue[0] != key:
                hashCode = self.hash(key, numberOfCollisions)
                index = self.Compressor(hashCode)
                possibleValue = self.array[index]
                if possibleValue is None:
                    return None
                if possibleValue[0] == key:
                    return possibleValue[1]
                number_collisions += 1
                return