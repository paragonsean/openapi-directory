/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRfeItemOptionVO.h
 *
 * Java type: com.noosh.nooshapi.vo.RfeItemOptionVO
 */

#ifndef OAIRfeItemOptionVO_H
#define OAIRfeItemOptionVO_H

#include <QJsonObject>

#include <QJsonValue>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIRfeItemOptionVO : public OAIObject {
public:
    OAIRfeItemOptionVO();
    OAIRfeItemOptionVO(QString json);
    ~OAIRfeItemOptionVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getItemOptionId() const;
    void setItemOptionId(const qint64 &item_option_id);
    bool is_item_option_id_Set() const;
    bool is_item_option_id_Valid() const;

    QJsonValue getQuantity() const;
    void setQuantity(const QJsonValue &quantity);
    bool is_quantity_Set() const;
    bool is_quantity_Valid() const;

    qint32 getQuantityIndex() const;
    void setQuantityIndex(const qint32 &quantity_index);
    bool is_quantity_index_Set() const;
    bool is_quantity_index_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_item_option_id;
    bool m_item_option_id_isSet;
    bool m_item_option_id_isValid;

    QJsonValue m_quantity;
    bool m_quantity_isSet;
    bool m_quantity_isValid;

    qint32 m_quantity_index;
    bool m_quantity_index_isSet;
    bool m_quantity_index_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRfeItemOptionVO)

#endif // OAIRfeItemOptionVO_H
