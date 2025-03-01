import numpy as np
import matplotlib.pyplot as plt
import argparse

# assumes labels are first column and features are subsequent columns
def load_data(tsv_path):
    dataset = np.loadtxt(tsv_path, delimiter='\t', encoding='utf-8')
    X, y = dataset[:, 1:], dataset[:, 0]
    return X, y

def main(data_in, num_epoch, learning_rate):
    X, y = load_data(data_in)
    raise NotImplementedError("nothing here yet")
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("data", type=str, help='path to data')
    parser.add_argument("num_epoch", type=int, help='number of epochs')
    parser.add_argument("learning_rate", type=float, help='learning rate')
    args = parser.parse_args()
    main(
        args.data_in,
        args.num_epoch,
        args.learning_rate
    )