# Imports
import random
import matplotlib.pyplot as plt


if __name__ == '__main__':

    # Definitions
    discreteTime = 10**6
    muVal = 0.75
    lambdaArr = [0.2, 0.4, 0.5, 0.6, 0.65, 0.7, 0.72, 0.74, 0.745]
    avgQueueDelays = []
    theoExpectedDelays = []
    
    for lambdaVal in lambdaArr:

        # Definitions
        queueLength = 0
        totalQueueLength = 0
        serverActive = False
        avgQueueLength = 0
        avgQueueDelay = 0
        theoExpectedDelay = 0
        theoLength = 0
        rho = 0

        for j in range(discreteTime):
            if random.random() < muVal and serverActive:    # if Mu is greater than random val and Server has packet in it
                serverActive = False                        # Packet Departs Server, goes offline
                if queueLength > 0:                         # If packets in Queue
                    queueLength -= 1                        # decrement Queue
                    serverActive = True                     # Activate server for new Packet

            if random.random() < lambdaVal:                 # if Lambda is greater than random val
                if not serverActive:                        # If server is Offline meaning queue is empty
                    serverActive = True                     # Add packet to server but don't increment queue
                else:
                    queueLength += 1                        # Else server is busy add packet to queue
            totalQueueLength += queueLength                 # add queue length to running total

        avgQueueLength = totalQueueLength / discreteTime    # Find average length
        avgQueueDelay = avgQueueLength / lambdaVal          # Calculate Average wait time Little's law W = L / λ
        avgQueueDelays.append(avgQueueDelay)

        rho = (lambdaVal * (1 - muVal)) / (muVal * (1 - lambdaVal)) # Find Rho so that you can calculate  Length
        theoLength = rho / (1 - rho)                                # Find length so you can calculate W
        theoExpectedDelay = theoLength / lambdaVal                  # Use Little's Law W = W = L / λ to find Theoretical Queueing Delay   
        theoExpectedDelays.append(theoExpectedDelay)                # Put that in array so that it can be used to plot 
        
        if lambdaVal == 0.2:                                # Just for Formatting
            print(f"------------------------------")
        
        print(f"Lambda: {lambdaVal}")
        print(f"Average Queue Length: {avgQueueLength:.1f}")
        print(f"Average Queueing Delay: {avgQueueDelay:.1f}")
        print(f"Theoretical Queueing Delay: {theoExpectedDelay:.1f}")
        print(f"------------------------------")
    
    # Plot, Expected Delay vs Arrival
    plt.figure(1, figsize=(15, 7))
    plt.plot(lambdaArr, avgQueueDelays, marker='o', color='orange')
    plt.title('Expected Queueing Delay vs Arrival Rate (λ)')
    plt.xlabel('Arrival Rate (λ)')
    plt.ylabel('Expected Queueing Delay')
    plt.grid(True)
    
    # Plot 2, Theoretical Delay as func of Arrival
    plt.figure(2, figsize=(15, 7))
    plt.plot(lambdaArr, theoExpectedDelays, marker='x', color='purple')
    plt.title('Theoretical Queueing Delay vs Arrival Rate (λ)')
    plt.xlabel('Arrival Rate (λ)')
    plt.ylabel('Theoretical Queueing Delay')
    plt.grid(True)
    

    # Plot 3, Overlay both
    plt.figure(3, figsize=(15, 7))
    plt.plot(lambdaArr, avgQueueDelays, marker='o', color='orange')
    plt.plot(lambdaArr, theoExpectedDelays, marker='x', color='purple')
    plt.title('Overlay Theoretical and Empirical')
    plt.xlabel('Arrival Rate (λ)')
    plt.ylabel('Theoretical and Empiral')
    plt.grid(True)
    plt.show()