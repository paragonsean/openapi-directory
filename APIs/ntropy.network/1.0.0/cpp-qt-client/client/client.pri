QT += network

HEADERS += \
# Models
    $${PWD}/OAIGetABatchOfBusinessTransactionClassificationResults_200_response.h \
    $${PWD}/OAIGetABatchOfBusinessTransactionClassificationResults_200_response_results_inner.h \
    $${PWD}/OAIGetABatchOfConsumerTransactionClassificationResults_200_response.h \
    $${PWD}/OAIGetABatchOfConsumerTransactionClassificationResults_200_response_results_inner.h \
    $${PWD}/OAIGetABatchOfConsumerTransactionClassificationResults_200_response_results_inner_contact.h \
    $${PWD}/OAIGetABatchOfConsumerTransactionClassificationResults_200_response_results_inner_location.h \
    $${PWD}/OAIGetABatchOfConsumerTransactionClassificationResults_200_response_results_inner_rating.h \
# APIs
    $${PWD}/OAIBatchApi.h \
    $${PWD}/OAIBatch1Api.h \
    $${PWD}/OAIBusinessApi.h \
    $${PWD}/OAIClassifierApi.h \
    $${PWD}/OAIConsumerApi.h \
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
    $${PWD}/OAIGetABatchOfBusinessTransactionClassificationResults_200_response.cpp \
    $${PWD}/OAIGetABatchOfBusinessTransactionClassificationResults_200_response_results_inner.cpp \
    $${PWD}/OAIGetABatchOfConsumerTransactionClassificationResults_200_response.cpp \
    $${PWD}/OAIGetABatchOfConsumerTransactionClassificationResults_200_response_results_inner.cpp \
    $${PWD}/OAIGetABatchOfConsumerTransactionClassificationResults_200_response_results_inner_contact.cpp \
    $${PWD}/OAIGetABatchOfConsumerTransactionClassificationResults_200_response_results_inner_location.cpp \
    $${PWD}/OAIGetABatchOfConsumerTransactionClassificationResults_200_response_results_inner_rating.cpp \
# APIs
    $${PWD}/OAIBatchApi.cpp \
    $${PWD}/OAIBatch1Api.cpp \
    $${PWD}/OAIBusinessApi.cpp \
    $${PWD}/OAIClassifierApi.cpp \
    $${PWD}/OAIConsumerApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
