/**
 * Chain49 API
 * Kickstart your next crypto project - extended trezor/blockbook API with 10+ blockchains available instantly and 50+ possible on request running on the finest hardware in Germany's best datacenters at Hetzner  Websocket only via api.chain49.com endpoint possible (RapidAPI does not support it yet)
 *
 * The version of the OpenAPI document: 2.0
 * Contact: contact@chain49.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetNFTMetaV2_200_response.h
 *
 * 
 */

#ifndef OAIGetNFTMetaV2_200_response_H
#define OAIGetNFTMetaV2_200_response_H

#include <QJsonObject>

#include "OAIGetNFTMetaV2_200_response_contractInfo.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetNFTMetaV2_200_response_contractInfo;

class OAIGetNFTMetaV2_200_response : public OAIObject {
public:
    OAIGetNFTMetaV2_200_response();
    OAIGetNFTMetaV2_200_response(QString json);
    ~OAIGetNFTMetaV2_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGetNFTMetaV2_200_response_contractInfo getContractInfo() const;
    void setContractInfo(const OAIGetNFTMetaV2_200_response_contractInfo &contract_info);
    bool is_contract_info_Set() const;
    bool is_contract_info_Valid() const;

    QString getTokenId() const;
    void setTokenId(const QString &token_id);
    bool is_token_id_Set() const;
    bool is_token_id_Valid() const;

    QString getUri() const;
    void setUri(const QString &uri);
    bool is_uri_Set() const;
    bool is_uri_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGetNFTMetaV2_200_response_contractInfo m_contract_info;
    bool m_contract_info_isSet;
    bool m_contract_info_isValid;

    QString m_token_id;
    bool m_token_id_isSet;
    bool m_token_id_isValid;

    QString m_uri;
    bool m_uri_isSet;
    bool m_uri_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNFTMetaV2_200_response)

#endif // OAIGetNFTMetaV2_200_response_H
