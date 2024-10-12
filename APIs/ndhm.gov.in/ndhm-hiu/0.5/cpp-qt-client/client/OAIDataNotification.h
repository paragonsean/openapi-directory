/**
 * Health Repository Provider Specifications for HIU
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **_/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **_/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **_/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDataNotification.h
 *
 * 
 */

#ifndef OAIDataNotification_H
#define OAIDataNotification_H

#include <QJsonObject>

#include "OAIDataNotification_entries_inner.h"
#include "OAIKeyMaterial.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDataNotification_entries_inner;
class OAIKeyMaterial;

class OAIDataNotification : public OAIObject {
public:
    OAIDataNotification();
    OAIDataNotification(QString json);
    ~OAIDataNotification() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIDataNotification_entries_inner> getEntries() const;
    void setEntries(const QList<OAIDataNotification_entries_inner> &entries);
    bool is_entries_Set() const;
    bool is_entries_Valid() const;

    OAIKeyMaterial getKeyMaterial() const;
    void setKeyMaterial(const OAIKeyMaterial &key_material);
    bool is_key_material_Set() const;
    bool is_key_material_Valid() const;

    qint32 getPageCount() const;
    void setPageCount(const qint32 &page_count);
    bool is_page_count_Set() const;
    bool is_page_count_Valid() const;

    qint32 getPageNumber() const;
    void setPageNumber(const qint32 &page_number);
    bool is_page_number_Set() const;
    bool is_page_number_Valid() const;

    QString getTransactionId() const;
    void setTransactionId(const QString &transaction_id);
    bool is_transaction_id_Set() const;
    bool is_transaction_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIDataNotification_entries_inner> m_entries;
    bool m_entries_isSet;
    bool m_entries_isValid;

    OAIKeyMaterial m_key_material;
    bool m_key_material_isSet;
    bool m_key_material_isValid;

    qint32 m_page_count;
    bool m_page_count_isSet;
    bool m_page_count_isValid;

    qint32 m_page_number;
    bool m_page_number_isSet;
    bool m_page_number_isValid;

    QString m_transaction_id;
    bool m_transaction_id_isSet;
    bool m_transaction_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDataNotification)

#endif // OAIDataNotification_H
