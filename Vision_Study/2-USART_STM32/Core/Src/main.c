/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2025 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "dma.h"
#include "usart.h"
#include "gpio.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */

/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
// *******************��/��������*******************
// ϵͳ��
#include <stdlib.h>
#include "string.h"
#include <stdio.h>
// �����
#include "OLED.h"
#include "Key.h"
// *******************ȫ�ֱ���*******************
// DMA���ڽ��ձ���
#define RX_USART1_LEN 50
uint8_t RX_USART1[RX_USART1_LEN] ;	// ��������
uint8_t RX_USART1_COPY[RX_USART1_LEN] ; // Copy����

// *******************ʵ������*******************
int check1 ;
int check2 ;
int check[50] ;

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_DMA_Init();
  MX_USART1_UART_Init();
  MX_USART2_UART_Init();
  /* USER CODE BEGIN 2 */
	
	// ******************* setup *******************
	// ����Systickʱ��
	HAL_SYSTICK_Config(SystemCoreClock / 1000);
	// ��ʼ��OLED
	OLED_Init() ;
	OLED_ShowString(0 , 0 , "Hello World" , OLED_8X16 ) ;
	// ����DMA+���տ����ж�,���յ����ݶ��洢��RX_USART1
	HAL_UARTEx_ReceiveToIdle_DMA(&huart1 , RX_USART1 , RX_USART1_LEN ) ;
	
	// ******************* ʵ������ *******************

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
		// ******************* while *******************
		// ���԰�������
		if (Key_Check(KEY_1 , KEY_SINGLE))
		{
			HAL_GPIO_TogglePin(LED0_GPIO_Port , LED0_Pin) ;
			
			Set_Current_USART(USART1_IDX); /* ��Ҫָ����ͬ���ڱ�����printfǰ���ϴ˺��� */
			printf("Serial=1\n");
		}
		else if (Key_Check(KEY_2 , KEY_SINGLE))
		{
			Set_Current_USART(USART2_IDX); /* ��Ҫָ����ͬ���ڱ�����printfǰ���ϴ˺��� */
			printf("Serial=2\n");
		}
		
		// ******************* ʵ������ *******************
		
		
		// �������:OLED����
		OLED_Update() ;
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.HSEPredivValue = RCC_HSE_PREDIV_DIV1;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL9;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
}

/* USER CODE BEGIN 4 */
// Systick��ʱ�ж�
void HAL_SYSTICK_Callback(void)
{
	// ��ʱ
	static int count_sys = 0 ;
	count_sys ++ ;
	// ����1:
	if (count_sys % 1000 == 0)
	{
//		HAL_GPIO_TogglePin(LED0_GPIO_Port , LED0_Pin ) ;
	}
	// ����2: ����
	Key_Tick() ;
}

// ���ڿ����жϻص�����
void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef *huart, uint16_t Size)
{
	if (huart->Instance == USART1)
	{
		// ����\0��ֹԽ��
		if (Size < RX_USART1_LEN)
		{
			RX_USART1[Size] = '\0';
		}     
		
		// ��������ʣ�����ݣ���ֹ�����ݲ���
    memset(RX_USART1 + Size, 0, RX_USART1_LEN - Size);
		
		// ���Ƶ���������
		memcpy(RX_USART1_COPY, RX_USART1, RX_USART1_LEN);
		
		// ���ͻ���
		HAL_UART_Transmit_DMA(&huart1, (uint8_t *)RX_USART1, Size);
		
		// ÿ�δ�������Ҫ���¿���DMA�ж�
		HAL_UARTEx_ReceiveToIdle_DMA(&huart1 , RX_USART1 , RX_USART1_LEN ) ;
	}
}
/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
