package com.herokuapp.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Currency {

    private static final long serialVersionUID = -8433157876767674682L;
    
    private Long id;

    private String from;

    private String to;

}