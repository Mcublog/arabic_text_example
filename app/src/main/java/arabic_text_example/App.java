/*
 * This Java source file was generated by the Gradle 'init' task.
 */

package arabic_text_example;

import java.nio.charset.Charset;
import java.text.Normalizer;

public class App {
    public String getGreeting() {
        // Иходная строка в UTF-8
        String stateOfQuatar = "شامبو ضد القشرة";
        // Реверсим строку, чтобы порядок байт был верный
        String stateOfQuatarRevers = new StringBuilder(stateOfQuatar).reverse().toString();
        byte[] strInBytes = stateOfQuatarRevers.getBytes(Charset.forName("CP1256"));
        for (int j=0; j<strInBytes.length; j++) {
           System.out.format("%02X ", strInBytes[j]);
        }
        System.out.println();
        System.out.println(stateOfQuatarRevers);
        System.out.println();
        System.out.println();

        // Удаление огласовок
        String hello = "مرحبًا"; //بً символ с огласовкой
        // Печатаем, как есть. Нужен реверс естественно
        System.err.println(new StringBuilder(hello).reverse().toString());
        // Печатаем без огласовок https://stackoverflow.com/questions/18580287/how-could-i-remove-arabic-punctuation-form-a-string-in-java
        hello = Normalizer.normalize(hello, Normalizer.Form.NFD).replaceAll("\\p{M}", "");
        System.err.println(new StringBuilder(hello).reverse().toString());
        return "";
    }

    public static void main(String[] args) {
        System.out.println(new App().getGreeting());
    }
}
