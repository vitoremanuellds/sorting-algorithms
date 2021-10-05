package algorithms.java_algorithms;

public class InsertionSort<T extends Comparable<T>> {
    
    public void sort(T[] item) {
        
        for (int i = 1; i < item.length; i++) {

            T auxElement = item[i];
            int k = i;

            while (k > 0 && item[k - 1].compareTo(auxElement) > 0) {

                item[k] = item[k-1];
                k--;
            }

            item[k] = auxElement;
        }
    }
}
