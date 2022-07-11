package com.herokuapp;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.herokuapp.model.Currency;
import com.herokuapp.usecase.addcurrency.AddCurrencyDto;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Application {

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        try {
            greetings(bw);
            String command = br.readLine();
            commands(command, br, bw);
            while (command.equalsIgnoreCase("")) {
                bw.write("\nYour command: ");
                bw.flush();
                command = br.readLine();
                commands(command, br, bw);
            }
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void greetings(BufferedWriter bw) throws IOException {
        bw.write("Welcome to the Foreign-Exchange CLI Application\n");
        bw.write("List of Command:\n");
        bw.write("1. Create Currency\n");
        bw.write("Your command: ");
        bw.flush();
    }

    private static void commands(
        String command,
        BufferedReader br,
        BufferedWriter bw
    ) throws IOException {
        switch (Integer.parseInt(command)) {
            case 1:
                create(br, bw);
                break;
            default:
                break;
        }
    }

    //TODO: Move into addcurrency package usecase
    private static void create(
        BufferedReader br,
        BufferedWriter bw
    ) throws IOException {
        bw.write("\nCurrency from: ");
        bw.flush();
        String from = br.readLine();
        bw.write("\nCurrency to: ");
        bw.flush();
        String to = br.readLine();
        file(bw, from, to);
    }

    //TODO: Move into repository package
    private static void file(BufferedWriter bw, String from, String to) throws IOException {
        File f = new File("src/main/resources/json/currency.json");
        ObjectMapper mapper = new ObjectMapper();
        List<Currency> example;
        if(f.exists() && !f.isDirectory()) {
            example = mapper.readValue(f, new TypeReference<List<Currency>>(){});
        } else {
            example = new ArrayList<Currency>();
        }
        example.add(new Currency((long) example.size(), from, to));
        String result = mapper.writeValueAsString(example);
        FileWriter writer = new FileWriter("src/main/resources/json/currency.json");
        writer.write(result);
        bw.write(mapper.writeValueAsString(AddCurrencyDto.success()));
        bw.flush();
        writer.close();
    }

}