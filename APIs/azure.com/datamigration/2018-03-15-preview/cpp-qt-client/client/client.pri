QT += network

HEADERS += \
# Models
    $${PWD}/OAIOperations_List_200_response.h \
    $${PWD}/OAIOperations_List_200_response_value_inner.h \
    $${PWD}/OAIOperations_List_200_response_value_inner_display.h \
    $${PWD}/OAIOperations_List_default_response.h \
    $${PWD}/OAIOperations_List_default_response_error.h \
    $${PWD}/OAIProjects_Get_200_response.h \
    $${PWD}/OAIProjects_List_200_response.h \
    $${PWD}/OAIProjects_List_200_response_value_inner.h \
    $${PWD}/OAIProjects_List_200_response_value_inner_properties.h \
    $${PWD}/OAIProjects_List_200_response_value_inner_properties_databasesInfo_inner.h \
    $${PWD}/OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo.h \
    $${PWD}/OAIResourceSkus_ListSkus_200_response.h \
    $${PWD}/OAIResourceSkus_ListSkus_200_response_value_inner.h \
    $${PWD}/OAIResourceSkus_ListSkus_200_response_value_inner_capabilities_inner.h \
    $${PWD}/OAIResourceSkus_ListSkus_200_response_value_inner_capacity.h \
    $${PWD}/OAIResourceSkus_ListSkus_200_response_value_inner_costs_inner.h \
    $${PWD}/OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner.h \
    $${PWD}/OAIServices_CheckNameAvailability_200_response.h \
    $${PWD}/OAIServices_CheckNameAvailability_request.h \
    $${PWD}/OAIServices_CheckStatus_200_response.h \
    $${PWD}/OAIServices_Get_200_response.h \
    $${PWD}/OAIServices_ListSkus_200_response.h \
    $${PWD}/OAIServices_ListSkus_200_response_value_inner.h \
    $${PWD}/OAIServices_ListSkus_200_response_value_inner_capacity.h \
    $${PWD}/OAIServices_ListSkus_200_response_value_inner_sku.h \
    $${PWD}/OAIServices_List_200_response.h \
    $${PWD}/OAIServices_List_200_response_value_inner.h \
    $${PWD}/OAIServices_List_200_response_value_inner_properties.h \
    $${PWD}/OAIServices_List_200_response_value_inner_sku.h \
    $${PWD}/OAITasks_Get_200_response.h \
    $${PWD}/OAITasks_List_200_response.h \
    $${PWD}/OAITasks_List_200_response_value_inner.h \
    $${PWD}/OAITasks_List_200_response_value_inner_properties.h \
    $${PWD}/OAIUsages_List_200_response.h \
    $${PWD}/OAIUsages_List_200_response_value_inner.h \
    $${PWD}/OAIUsages_List_200_response_value_inner_name.h \
# APIs
    $${PWD}/OAICustomOperationApi.h \
    $${PWD}/OAIDELETEApi.h \
    $${PWD}/OAIGETApi.h \
    $${PWD}/OAIPATCHApi.h \
    $${PWD}/OAIPOSTApi.h \
    $${PWD}/OAIPUTApi.h \
    $${PWD}/OAIProjectResourceApi.h \
    $${PWD}/OAIServiceResourceApi.h \
    $${PWD}/OAIStandardOperationApi.h \
    $${PWD}/OAITaskResourceApi.h \
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
    $${PWD}/OAIOperations_List_200_response.cpp \
    $${PWD}/OAIOperations_List_200_response_value_inner.cpp \
    $${PWD}/OAIOperations_List_200_response_value_inner_display.cpp \
    $${PWD}/OAIOperations_List_default_response.cpp \
    $${PWD}/OAIOperations_List_default_response_error.cpp \
    $${PWD}/OAIProjects_Get_200_response.cpp \
    $${PWD}/OAIProjects_List_200_response.cpp \
    $${PWD}/OAIProjects_List_200_response_value_inner.cpp \
    $${PWD}/OAIProjects_List_200_response_value_inner_properties.cpp \
    $${PWD}/OAIProjects_List_200_response_value_inner_properties_databasesInfo_inner.cpp \
    $${PWD}/OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo.cpp \
    $${PWD}/OAIResourceSkus_ListSkus_200_response.cpp \
    $${PWD}/OAIResourceSkus_ListSkus_200_response_value_inner.cpp \
    $${PWD}/OAIResourceSkus_ListSkus_200_response_value_inner_capabilities_inner.cpp \
    $${PWD}/OAIResourceSkus_ListSkus_200_response_value_inner_capacity.cpp \
    $${PWD}/OAIResourceSkus_ListSkus_200_response_value_inner_costs_inner.cpp \
    $${PWD}/OAIResourceSkus_ListSkus_200_response_value_inner_restrictions_inner.cpp \
    $${PWD}/OAIServices_CheckNameAvailability_200_response.cpp \
    $${PWD}/OAIServices_CheckNameAvailability_request.cpp \
    $${PWD}/OAIServices_CheckStatus_200_response.cpp \
    $${PWD}/OAIServices_Get_200_response.cpp \
    $${PWD}/OAIServices_ListSkus_200_response.cpp \
    $${PWD}/OAIServices_ListSkus_200_response_value_inner.cpp \
    $${PWD}/OAIServices_ListSkus_200_response_value_inner_capacity.cpp \
    $${PWD}/OAIServices_ListSkus_200_response_value_inner_sku.cpp \
    $${PWD}/OAIServices_List_200_response.cpp \
    $${PWD}/OAIServices_List_200_response_value_inner.cpp \
    $${PWD}/OAIServices_List_200_response_value_inner_properties.cpp \
    $${PWD}/OAIServices_List_200_response_value_inner_sku.cpp \
    $${PWD}/OAITasks_Get_200_response.cpp \
    $${PWD}/OAITasks_List_200_response.cpp \
    $${PWD}/OAITasks_List_200_response_value_inner.cpp \
    $${PWD}/OAITasks_List_200_response_value_inner_properties.cpp \
    $${PWD}/OAIUsages_List_200_response.cpp \
    $${PWD}/OAIUsages_List_200_response_value_inner.cpp \
    $${PWD}/OAIUsages_List_200_response_value_inner_name.cpp \
# APIs
    $${PWD}/OAICustomOperationApi.cpp \
    $${PWD}/OAIDELETEApi.cpp \
    $${PWD}/OAIGETApi.cpp \
    $${PWD}/OAIPATCHApi.cpp \
    $${PWD}/OAIPOSTApi.cpp \
    $${PWD}/OAIPUTApi.cpp \
    $${PWD}/OAIProjectResourceApi.cpp \
    $${PWD}/OAIServiceResourceApi.cpp \
    $${PWD}/OAIStandardOperationApi.cpp \
    $${PWD}/OAITaskResourceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
