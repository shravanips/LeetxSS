class Solution {
    public int reverse(int x) {
        int reversed = 0; // start by initial 0

        // for example 123
        while (x!=0) {
            // last digit -> to collect it
            int digit = x % 10; // we can get 3

            // remove or take out the last digit from the num (x)
            x = x / 10; // we get 12

            // overflow
            if (reversed > Integer.MAX_VALUE / 10 || (reversed == Integer.MAX_VALUE / 10 && digit > 7)) {
                return 0;
            } 


            // underflow - correct now 
            if (reversed < Integer.MIN_VALUE / 10 || (reversed == Integer.MIN_VALUE / 10 && digit <-8 )) {
                return 0;
            }

            //reverse number now last built 
            reversed = reversed * 10 + digit; // so this becomes 32 and digit become 1
        }

        return reversed;
    }
}