from django.http import HttpResponse
import math

def kopnina1_calculator(request):
    """
    Калькулятор для задачи 1004: размещение круглой сцены в квадратном зале
    """
    # Получаем параметры
    S_str = request.GET.get('S')
    R_str = request.GET.get('R')
    K_str = request.GET.get('K')
    
    # Если параметры не переданы, показываем форму
    if S_str is None or R_str is None or K_str is None:
        html = '''
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Kopnina1_response - Задача 1004</title>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body { 
                    background: linear-gradient(135deg, #43e97b 0%, #ff9a9e 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }
                .container { max-width: 700px; width: 90%; }
                .calculator { 
                    background: white; 
                    padding: 40px; 
                    border-radius: 20px;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                }
                h1 { 
                    color: #333; 
                    margin-bottom: 10px;
                    text-align: center;
                    font-size: 2em;
                }
                .subtitle {
                    color: #666;
                    text-align: center;
                    margin-bottom: 30px;
                    font-size: 1.1em;
                }
                .problem-badge {
                    background: #ff6b6b;
                    color: white;
                    padding: 8px 20px;
                    border-radius: 30px;
                    display: inline-block;
                    margin-bottom: 20px;
                    font-size: 1em;
                    font-weight: bold;
                }
                .input-group { margin-bottom: 20px; }
                .input-group label {
                    display: block;
                    margin-bottom: 8px;
                    color: #555;
                    font-weight: 600;
                }
                .input-group input {
                    width: 100%;
                    padding: 12px 15px;
                    border: 2px solid #e0e0e0;
                    border-radius: 10px;
                    font-size: 16px;
                    transition: border-color 0.3s;
                }
                .input-group input:focus {
                    outline: none;
                    border-color: #667eea;
                }
                .input-hint {
                    color: #999;
                    font-size: 0.85em;
                    margin-top: 5px;
                }
                button {
                    width: 100%;
                    padding: 15px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    border: none;
                    border-radius: 10px;
                    font-size: 1.1em;
                    font-weight: 600;
                    cursor: pointer;
                    transition: transform 0.2s, box-shadow 0.2s;
                }
                button:hover { 
                    transform: translateY(-2px);
                    box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
                }
                .examples { 
                    margin-top: 30px;
                    background: #f8f9fa;
                    padding: 20px;
                    border-radius: 10px;
                }
                .examples h3 {
                    color: #333;
                    margin-bottom: 15px;
                }
                .example-link {
                    display: inline-block;
                    margin: 5px;
                    padding: 8px 15px;
                    background: white;
                    color: #667eea;
                    text-decoration: none;
                    border-radius: 5px;
                    border: 1px solid #667eea;
                    transition: all 0.3s;
                }
                .example-link:hover {
                    background: #667eea;
                    color: white;
                }
                .footer {
                    text-align: center;
                    margin-top: 30px;
                    color: #999;
                    font-size: 0.9em;
                }
                .formula {
                    background: #f0f4f8;
                    padding: 15px;
                    border-radius: 10px;
                    margin-bottom: 25px;
                    text-align: center;
                    font-size: 1.1em;
                }
                .formula code {
                    background: #fff;
                    padding: 5px 10px;
                    border-radius: 5px;
                    color: #ff6b6b;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="calculator">
                    <div style="text-align: center;">
                        <span class="problem-badge">Задача 1004</span>
                    </div>
                    <h1>🏛️ Квадратный зал</h1>
                    <div class="subtitle">Можно ли разместить круглую сцену?</div>
                    
                    <div class="formula">
                        <strong>Условие:</strong> 
                        <code>2R + 2K ≤ √S</code>
                    </div>
                    
                    <form method="get" action="">
                        <div class="input-group">
                            <label>📐 Площадь зала (S):</label>
                            <input type="number" step="0.01" min="0.01" name="S" placeholder="Например: 100" required>
                            <div class="input-hint">квадратные единицы</div>
                        </div>
                        
                        <div class="input-group">
                            <label>⭕ Радиус сцены (R):</label>
                            <input type="number" step="0.01" min="0.01" name="R" placeholder="Например: 4" required>
                            <div class="input-hint">единицы длины</div>
                        </div>
                        
                        <div class="input-group">
                            <label>🚶 Ширина прохода (K):</label>
                            <input type="number" step="0.01" min="0" name="K" placeholder="Например: 1" required>
                            <div class="input-hint">минимальное расстояние от стены до сцены</div>
                        </div>
                        
                        <button type="submit">🔍 Проверить возможность размещения</button>
                    </form>
                    
                    <div class="examples">
                        <h3>📝 Примеры для проверки:</h3>
                        <div>
                            <a href="?S=100&R=4&K=1" class="example-link">S=100, R=4, K=1</a>
                            <a href="?S=100&R=5&K=1" class="example-link">S=100, R=5, K=1</a>
                            <a href="?S=64&R=3&K=1.5" class="example-link">S=64, R=3, K=1.5</a>
                            <a href="?S=144&R=5&K=2" class="example-link">S=144, R=5, K=2</a>
                            <a href="?S=50&R=3.5&K=1" class="example-link">S=50, R=3.5, K=1</a>
                        </div>
                    </div>
                    
                    <div class="footer">
                        VS Code · Django · Задача 1004 · Копнина
                    </div>
                </div>
            </div>
        </body>
        </html>
        '''
        return HttpResponse(html)
    
    # Если параметры переданы, решаем задачу
    try:
        S = float(S_str)
        R = float(R_str)
        K = float(K_str)
        
        # Проверка корректности
        if S <= 0 or R <= 0 or K < 0:
            error_msg = "Все значения должны быть положительными! (K может быть 0)"
            return error_response(error_msg)
        
        # Вычисления
        a = math.sqrt(S)  # сторона зала
        required_space = 2 * R + 2 * K  # необходимое пространство
        can_fit = required_space <= a
        difference = abs(a - required_space)
        
        # Визуализация в ASCII
        if can_fit:
            status_emoji = "✅"
            status_text = "ПОМЕЩАЕТСЯ"
            status_color = "#4CAF50"
        else:
            status_emoji = "❌"
            status_text = "НЕ ПОМЕЩАЕТСЯ"
            status_color = "#f44336"
        
        html = f'''
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Результат задачи 1004</title>
            <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{ 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    font-family: 'Segoe UI', sans-serif;
                    padding: 20px;
                }}
                .result-container {{
                    background: white;
                    padding: 40px;
                    border-radius: 20px;
                    max-width: 800px;
                    width: 100%;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                }}
                h1 {{
                    color: #333;
                    margin-bottom: 30px;
                    text-align: center;
                }}
                .status-badge {{
                    text-align: center;
                    padding: 20px;
                    background: {status_color};
                    color: white;
                    border-radius: 10px;
                    font-size: 1.8em;
                    font-weight: bold;
                    margin-bottom: 30px;
                }}
                .data-grid {{
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 20px;
                    margin-bottom: 30px;
                }}
                .data-item {{
                    background: #f8f9fa;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                }}
                .data-label {{
                    color: #666;
                    font-size: 0.9em;
                    margin-bottom: 5px;
                }}
                .data-value {{
                    font-size: 2em;
                    font-weight: bold;
                    color: #333;
                }}
                .data-unit {{
                    color: #999;
                    font-size: 0.8em;
                }}
                .calculation {{
                    background: #f0f4f8;
                    padding: 25px;
                    border-radius: 10px;
                    margin-bottom: 30px;
                }}
                .calculation h3 {{
                    color: #333;
                    margin-bottom: 15px;
                }}
                .formula-step {{
                    padding: 10px;
                    border-bottom: 1px solid #ddd;
                }}
                .formula-step:last-child {{
                    border-bottom: none;
                }}
                .visualization {{
                    background: #333;
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    font-family: monospace;
                    font-size: 1.2em;
                    line-height: 1.5;
                    text-align: center;
                    margin-bottom: 30px;
                }}
                .buttons {{
                    display: flex;
                    gap: 20px;
                }}
                .btn {{
                    flex: 1;
                    padding: 15px;
                    text-align: center;
                    text-decoration: none;
                    border-radius: 10px;
                    font-weight: bold;
                    transition: transform 0.2s;
                }}
                .btn-primary {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }}
                .btn-secondary {{
                    background: #f0f0f0;
                    color: #333;
                }}
                .btn:hover {{
                    transform: translateY(-2px);
                }}
                .conclusion {{
                    text-align: center;
                    font-size: 1.2em;
                    margin-top: 20px;
                    padding: 15px;
                    background: {status_color}20;
                    border-radius: 10px;
                    color: {status_color};
                }}
            </style>
        </head>
        <body>
            <div class="result-container">
                <h1>🏛️ Задача 1004: Результат</h1>
                
                <div class="status-badge">
                    {status_emoji} Сцена {status_text}
                </div>
                
                <div class="data-grid">
                    <div class="data-item">
                        <div class="data-label">Площадь зала (S)</div>
                        <div class="data-value">{S:.2f}</div>
                        <div class="data-unit">кв.ед.</div>
                    </div>
                    <div class="data-item">
                        <div class="data-label">Сторона зала (a = √S)</div>
                        <div class="data-value">{a:.2f}</div>
                        <div class="data-unit">ед.</div>
                    </div>
                    <div class="data-item">
                        <div class="data-label">Радиус сцены (R)</div>
                        <div class="data-value">{R:.2f}</div>
                        <div class="data-unit">ед.</div>
                    </div>
                    <div class="data-item">
                        <div class="data-label">Диаметр сцены (2R)</div>
                        <div class="data-value">{2*R:.2f}</div>
                        <div class="data-unit">ед.</div>
                    </div>
                    <div class="data-item">
                        <div class="data-label">Проход (K)</div>
                        <div class="data-value">{K:.2f}</div>
                        <div class="data-unit">ед.</div>
                    </div>
                    <div class="data-item">
                        <div class="data-label">Нужно места (2R+2K)</div>
                        <div class="data-value">{required_space:.2f}</div>
                        <div class="data-unit">ед.</div>
                    </div>
                </div>
                
                <div class="calculation">
                    <h3>📊 Проверка условия:</h3>
                    <div class="formula-step">
                        <strong>Шаг 1:</strong> Находим сторону зала: a = √{S:.2f} = {a:.2f}
                    </div>
                    <div class="formula-step">
                        <strong>Шаг 2:</strong> Вычисляем необходимое пространство: 2R + 2K = 2×{R:.2f} + 2×{K:.2f} = {required_space:.2f}
                    </div>
                    <div class="formula-step">
                        <strong>Шаг 3:</strong> Проверяем условие: {required_space:.2f} ≤ {a:.2f} ?
                    </div>
                    <div class="formula-step" style="font-weight: bold; color: {status_color};">
                        <strong>Результат:</strong> {required_space:.2f} {"≤" if can_fit else ">"} {a:.2f} → Сцена {status_text.lower()}
                    </div>
                </div>
                
                <div class="visualization">
                    {'✅' if can_fit else '❌'} Размещение сцены в зале:<br>
                    <br>
                    ┌────────────────────┐<br>
                    │                    │<br>
                    │      ┌──────┐      {('' if can_fit else '⚠️')}<br>
                    │      │  ⭕  │      │<br>
                    │      │  R   │      │<br>
                    │      └──────┘      │<br>
                    │                    │<br>
                    └────────────────────┘<br>
                    ←------- a = {a:.1f} -------→<br>
                    <br>
                    {'✓ Проход достаточный' if can_fit else f'✗ Не хватает {difference:.2f} ед.'}
                </div>
                
                <div class="conclusion">
                    {status_emoji} <strong>Итог:</strong> {'Сцена помещается в зал' if can_fit else 'Сцена НЕ помещается в зал'} 
                    {'с запасом ' + f'{difference:.2f}' if can_fit else f'. Не хватает {difference:.2f} ед.'}
                </div>
                
                <div class="buttons">
                    <a href="/kopnina1/" class="btn btn-primary">🔄 Новый расчет</a>
                    <a href="?S={S}&R={R}&K={K*0.9 if can_fit else K*1.1}" class="btn btn-secondary">🔧 Подобрать параметры</a>
                </div>
            </div>
        </body>
        </html>
        '''
        
    except ValueError:
        return error_response("Пожалуйста, введите корректные числа!")
    except Exception as e:
        return error_response(f"Ошибка вычисления: {str(e)}")
    
    return HttpResponse(html)


def error_response(message):
    """Функция для генерации страницы с ошибкой"""
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                background: linear-gradient(135deg, #ff6b6b 0%, #ff8e8e 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: 'Segoe UI', sans-serif;
            }}
            .error-box {{
                background: white;
                padding: 40px;
                border-radius: 20px;
                text-align: center;
                max-width: 400px;
                box-shadow: 0 20px 60px rgba(255,107,107,0.3);
            }}
            .error-icon {{
                font-size: 4em;
                margin-bottom: 20px;
            }}
            h1 {{
                color: #ff6b6b;
                margin-bottom: 20px;
            }}
            p {{
                color: #666;
                margin-bottom: 30px;
            }}
            a {{
                display: inline-block;
                padding: 12px 30px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-decoration: none;
                border-radius: 10px;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="error-box">
            <div class="error-icon">❌</div>
            <h1>Ошибка</h1>
            <p>{message}</p>
            <a href="/kopnina1/">Вернуться к калькулятору</a>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)


def kopnina1_home(request):
    """Домашняя страница с описанием задачи"""
    html = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Задача 1004 - Калькулятор Копниной</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: 'Segoe UI', sans-serif;
                padding: 20px;
            }
            .container {
                max-width: 900px;
                width: 100%;
                background: white;
                border-radius: 20px;
                padding: 50px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            }
            h1 {
                color: #333;
                font-size: 2.5em;
                margin-bottom: 20px;
                text-align: center;
            }
            .problem-card {
                background: #f8f9fa;
                border-radius: 15px;
                padding: 30px;
                margin: 30px 0;
            }
            .problem-number {
                background: #ff6b6b;
                color: white;
                padding: 5px 15px;
                border-radius: 25px;
                display: inline-block;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .problem-text {
                font-size: 1.2em;
                color: #333;
                margin-bottom: 20px;
                padding: 20px;
                background: white;
                border-radius: 10px;
                border-left: 5px solid #667eea;
            }
            .formula {
                background: #e3f2fd;
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
                text-align: center;
                font-size: 1.3em;
            }
            .formula code {
                background: white;
                padding: 5px 15px;
                border-radius: 5px;
                color: #ff6b6b;
                font-weight: bold;
            }
            .feature-grid {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
                margin: 30px 0;
            }
            .feature {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
            .feature h3 {
                color: #667eea;
                margin-bottom: 10px;
            }
            .btn {
                display: inline-block;
                padding: 15px 40px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-decoration: none;
                border-radius: 10px;
                font-size: 1.2em;
                font-weight: bold;
                transition: transform 0.2s;
                margin-top: 20px;
            }
            .btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
            }
            .footer {
                text-align: center;
                margin-top: 40px;
                color: #999;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧮 Калькулятор Копниной</h1>
            
            <div class="problem-card">
                <span class="problem-number">Задача №1004</span>
                
                <div class="problem-text">
                    <strong>Условие задачи:</strong><br>
                    Можно ли в квадратном зале площадью S поместить круглую сцену радиусом R 
                    так, чтобы от стены до сцены был проход не менее K?
                </div>
                
                <div class="formula">
                    <strong>Формула проверки:</strong><br>
                    <code>2R + 2K ≤ √S</code>
                </div>
                
                <div class="feature-grid">
                    <div class="feature">
                        <h3>📐 Что вводим:</h3>
                        <ul style="list-style-position: inside;">
                            <li><strong>S</strong> - площадь зала (м²)</li>
                            <li><strong>R</strong> - радиус сцены (м)</li>
                            <li><strong>K</strong> - ширина прохода (м)</li>
                        </ul>
                    </div>
                    <div class="feature">
                        <h3>✅ Что получаем:</h3>
                        <ul style="list-style-position: inside;">
                            <li>Помещается или нет</li>
                            <li>Детальные расчеты</li>
                            <li>Визуализацию</li>
                        </ul>
                    </div>
                </div>
                
                <div style="text-align: center;">
                    <a href="/kopnina1/calculator/" class="btn">🚀 Решить задачу</a>
                </div>
            </div>
            
            <div class="footer">
                VS Code · Django · Задача 1004 · Копнина v2.0
            </div>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)