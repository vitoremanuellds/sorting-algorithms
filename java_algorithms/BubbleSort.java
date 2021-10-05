package algorithms.java_algorithms;

public class BubbleSort<T extends Comparable<T>> {

    public void sort(T[] item) {
        for (int i = 0; i < item.length - 1; i++) {

            for (int k = 0; k < item.length - 1 - i; k++) {

                if (item[k].compareTo(item[k+1]) > 0) {
                    this.swap(item, k, k+1);
                }

            }

        }
    }

    private void swap(T[] item, int firstIndex, int secondIndex) {
        T aux = item[firstIndex];
        item[firstIndex] = item[secondIndex];
        item[secondIndex] = aux;
    }
    

}