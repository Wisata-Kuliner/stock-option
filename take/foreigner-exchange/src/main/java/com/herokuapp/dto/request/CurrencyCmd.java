package com.herokuapp.dto.request;

import lombok.Value;
import lombok.Builder;
import lombok.With;

@Value
@Builder
public class CurrencyCmd {

    @With
    Long id;

    String from;
    
    String to;

}