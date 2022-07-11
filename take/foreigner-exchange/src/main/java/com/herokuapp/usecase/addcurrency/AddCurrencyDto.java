package com.herokuapp.usecase.addcurrency;

import lombok.Builder;
import lombok.Value;

@Value
@Builder
public class AddCurrencyDto {

    boolean status;

    String message;

    public static AddCurrencyDto success() {
        return AddCurrencyDto.builder()
                .status(true)
                .message("Currency Inserted")
                .build();
    }

}