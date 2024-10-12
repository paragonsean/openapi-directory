QT += network

HEADERS += \
# Models
    $${PWD}/OAICategoriesEntity.h \
    $${PWD}/OAIChannelsEntity.h \
    $${PWD}/OAIError401.h \
    $${PWD}/OAIError403.h \
    $${PWD}/OAIError404.h \
    $${PWD}/OAIError422.h \
    $${PWD}/OAIError500.h \
    $${PWD}/OAIEventsCapacitiesEntity.h \
    $${PWD}/OAIEventsCapacitiesEntity_event_categories_inner.h \
    $${PWD}/OAIEventsCategoriesEntity.h \
    $${PWD}/OAIEventsCategoriesEntity_event_price_ranges_inner.h \
    $${PWD}/OAIEventsChannelsEntity.h \
    $${PWD}/OAIEventsEntity.h \
    $${PWD}/OAIEventsEntity_contract.h \
    $${PWD}/OAIEventsEntity_contract_partner.h \
    $${PWD}/OAIEventsEntity_contract_type.h \
    $${PWD}/OAIEventsEntity_input_type.h \
    $${PWD}/OAIPriceRangesEntity.h \
    $${PWD}/OAIPromotionsEntity.h \
    $${PWD}/OAIPromotionsEntity_applied_to_inner.h \
    $${PWD}/OAIPromotionsEntity_cost.h \
    $${PWD}/OAIPromotionsEntity_cost_state.h \
    $${PWD}/OAIPromotionsEntity_cost_type.h \
    $${PWD}/OAIPromotionsEntity_supplier.h \
    $${PWD}/OAIPromotionsEntity_type.h \
    $${PWD}/OAIPromotionsEntity_type_family.h \
    $${PWD}/OAISeriesEntity.h \
    $${PWD}/OAISeriesEntity_contract.h \
    $${PWD}/OAISeriesEntity_contract_partner.h \
    $${PWD}/OAISeriesEntity_contract_type.h \
    $${PWD}/OAISeriesEntity_type.h \
    $${PWD}/OAITicketCountsDetailedEntity.h \
    $${PWD}/OAITicketCountsDetailedEntity_event_channels_inner.h \
    $${PWD}/OAITicketCountsDetailedEntity_event_channels_inner_event_categories_inner.h \
    $${PWD}/OAITicketCountsDetailedEntity_event_channels_inner_event_categories_inner_event_price_ranges_inner.h \
    $${PWD}/OAITicketCountsEntity.h \
    $${PWD}/OAIVenuesEntity.h \
    $${PWD}/OAIVenuesEntity_type.h \
# APIs
    $${PWD}/OAICapacitiesApi.h \
    $${PWD}/OAICategoriesApi.h \
    $${PWD}/OAIChannelsApi.h \
    $${PWD}/OAICountsApi.h \
    $${PWD}/OAIEventsApi.h \
    $${PWD}/OAIPriceRangesApi.h \
    $${PWD}/OAIPromotionsApi.h \
    $${PWD}/OAISeriesApi.h \
    $${PWD}/OAIVenuesApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAICategoriesEntity.cpp \
    $${PWD}/OAIChannelsEntity.cpp \
    $${PWD}/OAIError401.cpp \
    $${PWD}/OAIError403.cpp \
    $${PWD}/OAIError404.cpp \
    $${PWD}/OAIError422.cpp \
    $${PWD}/OAIError500.cpp \
    $${PWD}/OAIEventsCapacitiesEntity.cpp \
    $${PWD}/OAIEventsCapacitiesEntity_event_categories_inner.cpp \
    $${PWD}/OAIEventsCategoriesEntity.cpp \
    $${PWD}/OAIEventsCategoriesEntity_event_price_ranges_inner.cpp \
    $${PWD}/OAIEventsChannelsEntity.cpp \
    $${PWD}/OAIEventsEntity.cpp \
    $${PWD}/OAIEventsEntity_contract.cpp \
    $${PWD}/OAIEventsEntity_contract_partner.cpp \
    $${PWD}/OAIEventsEntity_contract_type.cpp \
    $${PWD}/OAIEventsEntity_input_type.cpp \
    $${PWD}/OAIPriceRangesEntity.cpp \
    $${PWD}/OAIPromotionsEntity.cpp \
    $${PWD}/OAIPromotionsEntity_applied_to_inner.cpp \
    $${PWD}/OAIPromotionsEntity_cost.cpp \
    $${PWD}/OAIPromotionsEntity_cost_state.cpp \
    $${PWD}/OAIPromotionsEntity_cost_type.cpp \
    $${PWD}/OAIPromotionsEntity_supplier.cpp \
    $${PWD}/OAIPromotionsEntity_type.cpp \
    $${PWD}/OAIPromotionsEntity_type_family.cpp \
    $${PWD}/OAISeriesEntity.cpp \
    $${PWD}/OAISeriesEntity_contract.cpp \
    $${PWD}/OAISeriesEntity_contract_partner.cpp \
    $${PWD}/OAISeriesEntity_contract_type.cpp \
    $${PWD}/OAISeriesEntity_type.cpp \
    $${PWD}/OAITicketCountsDetailedEntity.cpp \
    $${PWD}/OAITicketCountsDetailedEntity_event_channels_inner.cpp \
    $${PWD}/OAITicketCountsDetailedEntity_event_channels_inner_event_categories_inner.cpp \
    $${PWD}/OAITicketCountsDetailedEntity_event_channels_inner_event_categories_inner_event_price_ranges_inner.cpp \
    $${PWD}/OAITicketCountsEntity.cpp \
    $${PWD}/OAIVenuesEntity.cpp \
    $${PWD}/OAIVenuesEntity_type.cpp \
# APIs
    $${PWD}/OAICapacitiesApi.cpp \
    $${PWD}/OAICategoriesApi.cpp \
    $${PWD}/OAIChannelsApi.cpp \
    $${PWD}/OAICountsApi.cpp \
    $${PWD}/OAIEventsApi.cpp \
    $${PWD}/OAIPriceRangesApi.cpp \
    $${PWD}/OAIPromotionsApi.cpp \
    $${PWD}/OAISeriesApi.cpp \
    $${PWD}/OAIVenuesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
