QT += network

HEADERS += \
# Models
    $${PWD}/OAIContext.h \
    $${PWD}/OAICreateUpdatePriceOrFixedPrice_request.h \
    $${PWD}/OAICreateorupdatefixedpricesonpricetableortradepolicy_request_inner.h \
    $${PWD}/OAIDateRange.h \
    $${PWD}/OAIDateRange_1.h \
    $${PWD}/OAIDateRange_2.h \
    $${PWD}/OAIFixedPrice.h \
    $${PWD}/OAIFixedPrices.h \
    $${PWD}/OAIGetPricingv2Status_200_response.h \
    $${PWD}/OAIGetallpricetablesandrules_200_response_inner.h \
    $${PWD}/OAIGetallpricetablesandrules_200_response_inner_rules_inner.h \
    $${PWD}/OAIGetallpricetablesandrules_200_response_inner_rules_inner_context.h \
    $${PWD}/OAIGetallpricetablesandrules_200_response_inner_rules_inner_context_dateRange.h \
    $${PWD}/OAIGetallpricetablesandrules_200_response_inner_rules_inner_context_markupRange.h \
    $${PWD}/OAIGetcomputedprice.h \
    $${PWD}/OAIGetprice.h \
    $${PWD}/OAIGetrulesforapricetable_200_response.h \
    $${PWD}/OAIMarkupRange.h \
    $${PWD}/OAIPricingConfiguration.h \
    $${PWD}/OAIPricingConfiguration_priceVariation.h \
    $${PWD}/OAIPricingConfiguration_tradePolicyConfigs_inner.h \
    $${PWD}/OAIRules_inner.h \
    $${PWD}/OAI_pricing_pipeline_catalog__priceTableId__put_request.h \
# APIs
    $${PWD}/OAIPriceTablesApi.h \
    $${PWD}/OAIPricesAndFixedPricesApi.h \
    $${PWD}/OAIPricingConfigurationApi.h \
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
    $${PWD}/OAIContext.cpp \
    $${PWD}/OAICreateUpdatePriceOrFixedPrice_request.cpp \
    $${PWD}/OAICreateorupdatefixedpricesonpricetableortradepolicy_request_inner.cpp \
    $${PWD}/OAIDateRange.cpp \
    $${PWD}/OAIDateRange_1.cpp \
    $${PWD}/OAIDateRange_2.cpp \
    $${PWD}/OAIFixedPrice.cpp \
    $${PWD}/OAIFixedPrices.cpp \
    $${PWD}/OAIGetPricingv2Status_200_response.cpp \
    $${PWD}/OAIGetallpricetablesandrules_200_response_inner.cpp \
    $${PWD}/OAIGetallpricetablesandrules_200_response_inner_rules_inner.cpp \
    $${PWD}/OAIGetallpricetablesandrules_200_response_inner_rules_inner_context.cpp \
    $${PWD}/OAIGetallpricetablesandrules_200_response_inner_rules_inner_context_dateRange.cpp \
    $${PWD}/OAIGetallpricetablesandrules_200_response_inner_rules_inner_context_markupRange.cpp \
    $${PWD}/OAIGetcomputedprice.cpp \
    $${PWD}/OAIGetprice.cpp \
    $${PWD}/OAIGetrulesforapricetable_200_response.cpp \
    $${PWD}/OAIMarkupRange.cpp \
    $${PWD}/OAIPricingConfiguration.cpp \
    $${PWD}/OAIPricingConfiguration_priceVariation.cpp \
    $${PWD}/OAIPricingConfiguration_tradePolicyConfigs_inner.cpp \
    $${PWD}/OAIRules_inner.cpp \
    $${PWD}/OAI_pricing_pipeline_catalog__priceTableId__put_request.cpp \
# APIs
    $${PWD}/OAIPriceTablesApi.cpp \
    $${PWD}/OAIPricesAndFixedPricesApi.cpp \
    $${PWD}/OAIPricingConfigurationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
