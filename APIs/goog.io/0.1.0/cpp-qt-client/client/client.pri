QT += network

HEADERS += \
# Models
    $${PWD}/OAICrawl_200_response.h \
    $${PWD}/OAIGet_the_status_of_the_API_service_200_response.h \
    $${PWD}/OAIHTTPValidationError.h \
    $${PWD}/OAIImages_200_response.h \
    $${PWD}/OAIImages_200_response_image_results_inner.h \
    $${PWD}/OAIImages_200_response_image_results_inner_image.h \
    $${PWD}/OAIImages_200_response_image_results_inner_link.h \
    $${PWD}/OAINews_200_response.h \
    $${PWD}/OAINews_200_response_entries_inner.h \
    $${PWD}/OAINews_200_response_feed.h \
    $${PWD}/OAISearch_200_response.h \
    $${PWD}/OAISearch_200_response_results_inner.h \
    $${PWD}/OAISerpData.h \
    $${PWD}/OAISerp_200_response.h \
    $${PWD}/OAIValidationError.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAICrawl_200_response.cpp \
    $${PWD}/OAIGet_the_status_of_the_API_service_200_response.cpp \
    $${PWD}/OAIHTTPValidationError.cpp \
    $${PWD}/OAIImages_200_response.cpp \
    $${PWD}/OAIImages_200_response_image_results_inner.cpp \
    $${PWD}/OAIImages_200_response_image_results_inner_image.cpp \
    $${PWD}/OAIImages_200_response_image_results_inner_link.cpp \
    $${PWD}/OAINews_200_response.cpp \
    $${PWD}/OAINews_200_response_entries_inner.cpp \
    $${PWD}/OAINews_200_response_feed.cpp \
    $${PWD}/OAISearch_200_response.cpp \
    $${PWD}/OAISearch_200_response_results_inner.cpp \
    $${PWD}/OAISerpData.cpp \
    $${PWD}/OAISerp_200_response.cpp \
    $${PWD}/OAIValidationError.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
