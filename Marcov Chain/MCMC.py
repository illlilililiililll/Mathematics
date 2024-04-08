import numpy as np
import matplotlib.pyplot as plt

def MCMC(num_steps, transition_matrix):
    current_state = 0
    state_counts = [0, 0]
    probabilities = []

    for i in range(1, num_steps + 1):
        current_state = np.random.choice([0, 1], p=transition_matrix[current_state])
        state_counts[current_state] += 1
        probabilities.append([state_counts[0] / i, state_counts[1] / i])

    return probabilities

if __name__ == '__main__':
    try:
        paa, pab = map(float, input('A -> A, A -> B 확률을 입력하세요 ex. 0.7 0.3\n: ').split())
        pba, pbb = map(float, input('B -> A, B -> B 확률을 입력하세요 ex. 0.7 0.3\n: ').split())
    except ValueError:
        print("잘못된 입력입니다. 다시 시도하세요.")

    else:
        p = np.array([[paa, pab], [pba, pbb]])

        num_steps = 10000
        
        probabilities = MCMC(num_steps, p)

        probabilities = np.array(probabilities)
        fig, axs = plt.subplots(2, 1, figsize=(9, 5))

        axs[0].plot(probabilities[:, 0], color='b')
        axs[0].set_title('A')
        axs[0].set_xlabel('State')
        axs[0].set_ylabel('Probability')

        axs[1].plot(probabilities[:, 1], color='o')
        axs[1].set_title('B')
        axs[1].set_xlabel('State')
        axs[1].set_ylabel('Probability')

        plt.suptitle('Marcov Chain Monte Carlo', fontsize=16)
        plt.tight_layout()
        plt.show()

        final_prob_A, final_prob_B = probabilities[-1]
        print("마지막 시행 후 상태 A의 확률: {.4f}".format(final_prob_A))
        print("마지막 시행 후 상태 B의 확률: {.4f}".format(final_prob_B))