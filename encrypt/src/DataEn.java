/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.util.logging.Level;
import java.util.logging.Logger;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

/**
 *
 * @author yzw
 */
public class DataEn {

    private static SecretKey secretKey;
    private static final String AES = "AES";

    static {
        try {
            secretKey = new SecretKeySpec(Base64.decode("8iLUnz1tcbfGwApQcpr2AQ==", 4), AES);
        } catch (Exception ex) {
        }
    }

    /**
     * 加密
     *
     * @param data 待加密数据
     * @return
     * @throws Exception
     */
    public static String encrypt(String data) throws Exception {
        byte[] endata = encrypt(data.getBytes());
        return Base64.encodeToString(endata, Base64.CRLF);
    }

    /**
     * 解密
     *
     * @param data 待解密数据
     * @return
     * @throws Exception
     */
    public static String decrypt(String data) throws Exception {
        byte be[] = Base64.decode(data, Base64.CRLF);
        return new String(decrypt(be));
    }

    private static byte[] encrypt(byte[] data) throws Exception {
        if (null == secretKey) {
            throw new SecurityException("secretKey is null");
        }
        Cipher cipher = Cipher.getInstance(secretKey.getAlgorithm());
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        return cipher.doFinal(data);
    }

    private static byte[] decrypt(byte[] data) throws Exception {
        if (null == secretKey) {
            throw new SecurityException("secretKey is null");
        }
        Cipher cipher = Cipher.getInstance(secretKey.getAlgorithm());
        cipher.init(Cipher.DECRYPT_MODE, secretKey);
        return cipher.doFinal(data);
    }
    public static void main(String[] args) throws Exception {

    }
}
