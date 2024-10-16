/**
 * Neblio REST API Suite
 * APIs for Interacting with NTP1 Tokens & The Neblio Blockchain
 *
 * The version of the OpenAPI document: 1.3.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData.h
 *
 * Metadata set by user on token
 */

#ifndef OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData_H
#define OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData_H

#include <QJsonObject>

#include "OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData_meta_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData_meta_inner;

class OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData : public OAIObject {
public:
    OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData();
    OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData(QString json);
    ~OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData_meta_inner> getMeta() const;
    void setMeta(const QList<OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData_meta_inner> &meta);
    bool is_meta_Set() const;
    bool is_meta_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData_meta_inner> m_meta;
    bool m_meta_isSet;
    bool m_meta_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData)

#endif // OAIGetTokenMetadataResponse_metadataOfIssuance_data_userData_H
