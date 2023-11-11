/*
 * This Java source file was generated by the Gradle 'init' task.
 */

package arabic_text_example;

import java.nio.charset.Charset;

public class App {
    public String getGreeting() {
        // Иходная строка в UTF-8
        String stateOfQuatar = "دولة قطر";
        // Реверсим строку, чтобы порядок байт был верный
        String stateOfQuatarRevers = new StringBuilder(stateOfQuatar).reverse().toString();
        byte[] strInBytes = stateOfQuatarRevers.getBytes(Charset.forName("CP1256"));
        for (int j=0; j<strInBytes.length; j++) {
           System.out.format("%02X ", strInBytes[j]);
        }
        System.out.println("\n");
        return stateOfQuatar;
    }

    public static void main(String[] args) {
        System.out.println(new App().getGreeting());
    }
}
