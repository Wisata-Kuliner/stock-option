package com.herokuapp.dto.request;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class CurrencyCmdTest {

    @Test
    void testAttributeShouldReturnCorrectResult() {
        CurrencyCmd cmd = mockCmd();

        assertEquals("USD", cmd.getFrom());
        assertEquals("GBP", cmd.getTo());
    }

    private CurrencyCmd mockCmd() {
        return CurrencyCmd.builder()
            .from("USD")
            .to("GBP")
            .build();
    }

}