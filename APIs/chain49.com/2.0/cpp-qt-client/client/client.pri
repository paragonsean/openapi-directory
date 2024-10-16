QT += network

HEADERS += \
# Models
    $${PWD}/OAIGetBalanceHistoryV2_200_response_inner.h \
    $${PWD}/OAIGetBlockHashV2_200_response.h \
    $${PWD}/OAIGetBlockV2_200_response.h \
    $${PWD}/OAIGetBlockV2_200_response_txs_inner.h \
    $${PWD}/OAIGetBlockV2_200_response_txs_inner_vin_inner.h \
    $${PWD}/OAIGetBlockV2_200_response_txs_inner_vout_inner.h \
    $${PWD}/OAIGetBlockchain_200_response.h \
    $${PWD}/OAIGetBlockchain_200_response_backend.h \
    $${PWD}/OAIGetBlockchain_200_response_blockbook.h \
    $${PWD}/OAIGetEstimateFeeV2_200_response.h \
    $${PWD}/OAIGetMempoolV2_200_response.h \
    $${PWD}/OAIGetMempoolV2_200_response_mempool_inner.h \
    $${PWD}/OAIGetNFTMetaV2_200_response.h \
    $${PWD}/OAIGetNFTMetaV2_200_response_contractInfo.h \
    $${PWD}/OAIGetRawBlockV2_200_response.h \
    $${PWD}/OAIGetTickersListV2_200_response.h \
    $${PWD}/OAIGetTickersV2_200_response.h \
    $${PWD}/OAIGetTransactionV2_200_response.h \
    $${PWD}/OAIGetTransactionV2_200_response_vin_inner.h \
    $${PWD}/OAIGetTransactionV2_200_response_vout_inner.h \
    $${PWD}/OAIGetXpubV2_200_response.h \
    $${PWD}/OAIGetXpubV2_200_response_tokens_inner.h \
    $${PWD}/OAIPostSendTxV2_200_response.h \
# APIs
    $${PWD}/OAIAddressesApi.h \
    $${PWD}/OAIBlocksApi.h \
    $${PWD}/OAIFeeEstimationApi.h \
    $${PWD}/OAINFTApi.h \
    $${PWD}/OAIStatusApi.h \
    $${PWD}/OAITickersApi.h \
    $${PWD}/OAITransactionsApi.h \
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
    $${PWD}/OAIGetBalanceHistoryV2_200_response_inner.cpp \
    $${PWD}/OAIGetBlockHashV2_200_response.cpp \
    $${PWD}/OAIGetBlockV2_200_response.cpp \
    $${PWD}/OAIGetBlockV2_200_response_txs_inner.cpp \
    $${PWD}/OAIGetBlockV2_200_response_txs_inner_vin_inner.cpp \
    $${PWD}/OAIGetBlockV2_200_response_txs_inner_vout_inner.cpp \
    $${PWD}/OAIGetBlockchain_200_response.cpp \
    $${PWD}/OAIGetBlockchain_200_response_backend.cpp \
    $${PWD}/OAIGetBlockchain_200_response_blockbook.cpp \
    $${PWD}/OAIGetEstimateFeeV2_200_response.cpp \
    $${PWD}/OAIGetMempoolV2_200_response.cpp \
    $${PWD}/OAIGetMempoolV2_200_response_mempool_inner.cpp \
    $${PWD}/OAIGetNFTMetaV2_200_response.cpp \
    $${PWD}/OAIGetNFTMetaV2_200_response_contractInfo.cpp \
    $${PWD}/OAIGetRawBlockV2_200_response.cpp \
    $${PWD}/OAIGetTickersListV2_200_response.cpp \
    $${PWD}/OAIGetTickersV2_200_response.cpp \
    $${PWD}/OAIGetTransactionV2_200_response.cpp \
    $${PWD}/OAIGetTransactionV2_200_response_vin_inner.cpp \
    $${PWD}/OAIGetTransactionV2_200_response_vout_inner.cpp \
    $${PWD}/OAIGetXpubV2_200_response.cpp \
    $${PWD}/OAIGetXpubV2_200_response_tokens_inner.cpp \
    $${PWD}/OAIPostSendTxV2_200_response.cpp \
# APIs
    $${PWD}/OAIAddressesApi.cpp \
    $${PWD}/OAIBlocksApi.cpp \
    $${PWD}/OAIFeeEstimationApi.cpp \
    $${PWD}/OAINFTApi.cpp \
    $${PWD}/OAIStatusApi.cpp \
    $${PWD}/OAITickersApi.cpp \
    $${PWD}/OAITransactionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
