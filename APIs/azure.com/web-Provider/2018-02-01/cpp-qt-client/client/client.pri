QT += network

HEADERS += \
# Models
    $${PWD}/OAIApplicationStack.h \
    $${PWD}/OAIApplicationStackCollection.h \
    $${PWD}/OAIProvider_GetAvailableStacks_default_response.h \
    $${PWD}/OAIProvider_GetAvailableStacks_default_response_error.h \
    $${PWD}/OAIProvider_GetAvailableStacks_default_response_error_details_inner.h \
    $${PWD}/OAIProvider_ListOperations_200_response.h \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner.h \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_display.h \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_properties.h \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_properties_serviceSpecification.h \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_properties_serviceSpecification_logSpecifications_inner.h \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_properties_serviceSpecification_metricSpecifications_inner.h \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_properties_serviceSpecification_metricSpecifications_inner_availabilities_inner.h \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_properties_serviceSpecification_metricSpecifications_inner_dimensions_inner.h \
    $${PWD}/OAIStackMajorVersion.h \
    $${PWD}/OAIStackMinorVersion.h \
# APIs
    $${PWD}/OAIProviderApi.h \
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
    $${PWD}/OAIApplicationStack.cpp \
    $${PWD}/OAIApplicationStackCollection.cpp \
    $${PWD}/OAIProvider_GetAvailableStacks_default_response.cpp \
    $${PWD}/OAIProvider_GetAvailableStacks_default_response_error.cpp \
    $${PWD}/OAIProvider_GetAvailableStacks_default_response_error_details_inner.cpp \
    $${PWD}/OAIProvider_ListOperations_200_response.cpp \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner.cpp \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_display.cpp \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_properties.cpp \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_properties_serviceSpecification.cpp \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_properties_serviceSpecification_logSpecifications_inner.cpp \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_properties_serviceSpecification_metricSpecifications_inner.cpp \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_properties_serviceSpecification_metricSpecifications_inner_availabilities_inner.cpp \
    $${PWD}/OAIProvider_ListOperations_200_response_value_inner_properties_serviceSpecification_metricSpecifications_inner_dimensions_inner.cpp \
    $${PWD}/OAIStackMajorVersion.cpp \
    $${PWD}/OAIStackMinorVersion.cpp \
# APIs
    $${PWD}/OAIProviderApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
