# Имитируем внешнюю зависимость (как будто это импорт из другого модуля)
class Database:
    def get_user_by_id(self, user_id):
        # В реальном коде здесь был бы SQL-запрос или вызов API
        return None  # Заглушка

# Глобальный экземпляр (как в реальном приложении)
db = Database()

def get_user_name(user_id):
    user = db.get_user_by_id(user_id)
    return user.name if user else "Unknown"

def test_get_user_name_with_mock():
    # ARRANGE
    mock_db = Mock()
    mock_user = Mock()
    mock_user.name = "Alice"
    mock_db.get_user_by_id.return_value = mock_user
    
    # ACT - Подменяем глобальную переменную db
    with patch('__main__.db', mock_db):
        result = get_user_name(123)
    
    # ASSERT
    assert result == "Alice"
    print("✅ Тест пройден! Результат:", result)
