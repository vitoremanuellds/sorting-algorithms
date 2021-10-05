package algorithms.java_algorithms;

public class SelectionSort<T extends Comparable<T>> {
    
    public void sort(T[] item) {
        for (int i = 0; i < item.length - 1; i++) {

            int smallest = i;

            for (int k = i; k < item.length; k++) {

                if (item[k].compareTo(item[smallest]) < 0) {
                    smallest = k;
                }

            }

            this.swap(item, i, smallest);
        }
    }

    private void swap(T[] item, int firstIndex, int secondIndex) {
        T aux = item[firstIndex];
        item[firstIndex] = item[secondIndex];
        item[secondIndex] = aux;
    }

}
