package com.herokuapp.dto.request;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class CurrencyCmdTest {

    @Test
    void testAttributeShouldReturnCorrectResult() {
        CurrencyCmd cmd = mockCmd();

        assertEquals("USD", cmd.getFrom());
        assertEquals("GBP", cmd.getTo());

        assertEquals(1L, cmd.withId(1L).getId());
    }

    @Test
    void valueShouldReturnCorrectResult() {
        CurrencyCmd.CurrencyCmdBuilder builder = CurrencyCmd.builder()
                .id(1L)
                .from("USD")
                .to("GBP");
        CurrencyCmd other =  mockCmd()
                .withId(1L);
        assertEquals("CurrencyCmd.CurrencyCmdBuilder(id=1, from=USD, to=GBP)", builder.toString());
        assertEquals("CurrencyCmd(id=null, from=USD, to=GBP)", mockCmd().toString());
        assertEquals(5400653, mockCmd().hashCode());
        assertEquals(5254451, other.hashCode());
        assertEquals(other, builder.build());
    }

    private CurrencyCmd mockCmd() {
        return CurrencyCmd.builder()
            .from("USD")
            .to("GBP")
            .build();
    }

}