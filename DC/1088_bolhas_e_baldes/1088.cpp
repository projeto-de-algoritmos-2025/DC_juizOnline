#include <iostream>
#include <vector>
using namespace std;

long long merge_count(vector<int>& arr, vector<int>& temp, int left, int mid, int right) {
    long long inv_count = 0;
    int i = left, j = mid + 1, k = left;
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) temp[k++] = arr[i++];
        else {
            temp[k++] = arr[j++];
            inv_count += (mid - i + 1);
        }
    }
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];
    for (i = left; i <= right; i++) arr[i] = temp[i];
    return inv_count;
}

long long merge_sort_count(vector<int>& arr, vector<int>& temp, int left, int right) {
    long long inv_count = 0;
    if (left < right) {
        int mid = (left + right) / 2;
        inv_count += merge_sort_count(arr, temp, left, mid);
        inv_count += merge_sort_count(arr, temp, mid + 1, right);
        inv_count += merge_count(arr, temp, left, mid, right);
    }
    return inv_count;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    while (true) {
        int n;
        cin >> n;
        if (n == 0) break;
        vector<int> arr(n), temp(n);
        for (int i = 0; i < n; i++) cin >> arr[i];
        long long inv = merge_sort_count(arr, temp, 0, n - 1);
        cout << (inv % 2 == 0 ? "Carlos" : "Marcelo") << '\n';
    }
    return 0;
}